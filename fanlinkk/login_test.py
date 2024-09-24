import os
import logging
from PySide6.QtCore import QUrl, QTimer, Signal, Slot
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView 
import db_utils  # Import the database utility file
import requests
import json
from Login import LoginPage
from token_utils import TokenUtils

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class BrowserApp(QWidget):
    login_successful = Signal()  # Define the signal
    def __init__(self, displayname, email, passwd, profile_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Fanvue Login")
        self.resize(1200, 800)
        self.token_utils = TokenUtils()
        self.displayname = displayname
        self.email = email
        self.passwd = passwd
        self.session = requests.Session()  # Initialize the session object
        self.jwt_token = None
        logging.info("BrowserApp initialized with credentials: %s, %s", self.displayname, self.email)
        self.profile = QWebEngineProfile(profile_name, self)  # Each browser has a unique profile name
        self.page = QWebEnginePage(self.profile, self)  # The profile is applied here

        # Setup the web view and layout
        self.web_view = QWebEngineView()
        self.web_view.setPage(self.page)
        self.web_view.setUrl(QUrl("https://fanvue.com/signin"))

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)

        self.setLayout(layout)

        self.web_view.loadFinished.connect(self.insert_login_details)
        self.web_view.urlChanged.connect(self.check_url)
        self.web_view.page().profile().cookieStore().cookieAdded.connect(self.save_csrf_cookies)
        self.web_view.page().profile().cookieStore().cookieAdded.connect(self.save_auth_cookies)

        self.csrf_dict = {}  # Dictionary to store csrf cookies
        self.auth_dict = {}  # Dictionary to store auth cookies
        self.last_csrf_token = None  # Variable to store the last csrf token
        self.last_auth_token = None  # Variable to store the last auth token

    def clear_browser_data(self):
        profile = self.web_view.page().profile()
        profile.clearHttpCache()
        profile.cookieStore().deleteAllCookies()
        profile.clearAllVisitedLinks()
    def clear_session(self):
        """Reset session and cookies"""
        self.session.cookies.clear()  # Clear the cookies from the session
        self.session = requests.Session()  # Reinitialize the session
        logging.info("Session and cookies cleared.")
    

    def insert_login_details(self):
        logging.info("Inserting login details.")
        js_code = f"""
            console.log("Running login script...");
            var interval = setInterval(function() {{
                var usernameField = document.querySelector('input[name="email"]');
                var passwordField = document.querySelector('input[name="password"]');
                console.log("Checking for fields...");
                if (usernameField && passwordField) {{
                    console.log("Fields found!");
                    usernameField.value = "{self.email}";
                    passwordField.value = "{self.passwd}";
                    
                    var event = new Event('input', {{ bubbles: true }});
                    usernameField.dispatchEvent(event);
                    passwordField.dispatchEvent(event);

                    event = new Event('change', {{ bubbles: true }});
                    usernameField.dispatchEvent(event);
                    passwordField.dispatchEvent(event);

                    var submitButton = document.querySelector('button[type="submit"]');
                    if (submitButton) {{
                        submitButton.click();
                    }}

                    clearInterval(interval);
                }} else {{
                    console.log("Fields not found, retrying...");
                }}
            }}, 100);
        """
        self.web_view.page().runJavaScript(js_code)

    def check_url(self, url):
        logging.info("Current URL: %s", url.toString())
        if url.toString().endswith("/home"):
            logging.info("Login successful.")
            QTimer.singleShot(2000, self.finalize_login)

    def finalize_login(self):
        self.clear_session()
        self.save_last_csrf_token()
        self.save_last_auth_token()
        #self.print_cookies()
        self.upload_to_database()
        self.login_successful.emit()  # Emit the signal when login is successful
        self.clear_browser_data()

    def save_csrf_cookies(self, cookie):
        cookie_name = cookie.name().data().decode('utf-8')
        cookie_value = cookie.value().data().decode('utf-8')
        
        if '_Host-next-auth.csrf-token' in cookie_name:
            self.csrf_dict[cookie_name] = cookie_value
            #logging.info("CSRF Cookie saved: %s: %s", cookie_name, cookie_value)

    def save_auth_cookies(self, cookie):
        cookie_name = cookie.name().data().decode('utf-8')
        cookie_value = cookie.value().data().decode('utf-8')
        
        if 'fv-auth.session-token' in cookie_name:
            self.auth_dict[cookie_name] = cookie_value
            #logging.info("Auth Cookie saved: %s: %s", cookie_name, cookie_value)

    def save_last_csrf_token(self):
        #logging.info("Attempting to save last CSRF token...")
        if '__Host-next-auth.csrf-token' in self.csrf_dict:
            self.last_csrf_token = self.csrf_dict['__Host-next-auth.csrf-token']
            #logging.info("Last CSRF token saved: %s", self.last_csrf_token)
        else:
            logging.warning("No CSRF token found to save.")

    def save_last_auth_token(self):
        #logging.info("Attempting to save last Auth token...")
        if 'fv-auth.session-token' in self.auth_dict:
            self.last_auth_token = self.auth_dict['fv-auth.session-token']
            #logging.info("Last auth token saved: %s", self.last_auth_token)
        else:
            logging.warning("No Auth token found to save.")

    def print_cookies(self):
        logging.info("CSRF Cookies: %s", self.csrf_dict)
        logging.info("Auth Cookies: %s", self.auth_dict)

    def upload_to_server(self, model_name, model_email, csrf_token, auth_token, jwt_token, refresh_token):
        url = 'http://127.0.0.1:8000/api/add_model/'
        data = {
            "model_name": model_name,
            "model_email": model_email,
            "csrf_token": csrf_token,
            "auth_token": auth_token
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {jwt_token}'  # Use the JWT access token here
        }

        logging.info("Uploading model with name: %s and email: %s", model_name, model_email)

        try:
            logging.debug(f"Sending data to server: {data}")
            response = self.session.post(url, json=data, headers=headers)

            # If the token has expired, handle the 401 error and refresh the token
            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                refreshed = self.token_utils.refresh_access_token(refresh_token)
                if refreshed:
                    # Retry the request with the new access token
                    headers['Authorization'] = f'Bearer {self.new_access_token}'
                    response = self.session.post(url, json=data, headers=headers)
                else:
                    print("Failed to refresh access token.")
                    return

            # Handle the response
            if response.status_code == 200:
                print("Model uploaded successfully!")
            elif response.status_code == 400:
                error_message = response.json().get('error')
                if error_message == 'Model is already registered by you':
                    print("Error: This model is already registered by you.")
                elif error_message == 'Model is already registered by another user':
                    print("Error: This model is already registered by another user.")
                else:
                    print(f"Error: {error_message}")
            else:
                print(f"Error uploading model: {response.text}")
        except Exception as e:
            logging.error(f"Error while uploading data: {e}")

    
    # def refresh_access_token(self, refresh_token):
    #     """Handles the logic for refreshing the access token."""
    #     refresh_url = 'http://127.0.0.1:8000/api/token/refresh/'
    #     data = {'refresh': refresh_token}
    #     try:
    #         response = self.session.post(refresh_url, json=data)
    #         if response.status_code == 200:
    #             new_access_token = response.json().get('access')
    #             logging.info("Access token refreshed successfully.")
    #             return new_access_token  # Return the token
    #         else:
    #             logging.error(f"Failed to refresh access token: {response.text}")
    #             return None
    #     except Exception as e:
    #         logging.error(f"Error refreshing token: {e}")
    #         return None

    def upload_to_database(self):
        """Uploads model details to the Django server using JWT token for authentication."""
        try:
            with open("session.json", "r") as session_file:
                session_data = json.load(session_file)
                jwt_token = session_data.get('access_token')
                refresh_token = session_data.get('refresh_token')  # Add refresh token
        except FileNotFoundError:
            print("Session file not found. Please log in again.")
            return

        if not jwt_token or not refresh_token:
            print("No JWT token or refresh token found. Please log in again.")
            return

        if self.last_auth_token and self.last_csrf_token:
            model_name = self.displayname
            model_email = self.email
            auth_token = self.last_auth_token
            csrf_token = self.last_csrf_token
            self.upload_to_server(model_name, model_email, csrf_token, auth_token, jwt_token, refresh_token)
        else:
            logging.error("Missing token, cannot upload model details to server.")


def run_browser_app(displayname, email, passwd):
    logging.info("Running BrowserApp with credentials: %s, %s", displayname, email)
    profile_name = "default_profile"  # Define a default or dynamic profile name here
    browser_app = BrowserApp(displayname, email, passwd, profile_name)
    browser_app.show()
    return browser_app
