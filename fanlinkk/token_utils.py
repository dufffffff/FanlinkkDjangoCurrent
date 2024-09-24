import requests
import logging
import json
class TokenUtils:
        
    def refresh_access_token(refresh_token):
        """Handles the logic for refreshing the access token."""
        refresh_url = 'http://127.0.0.1:8000/api/token/refresh/'
        data = {'refresh': refresh_token}
        try:
            session = requests.Session()  # Create a session if needed
            response = session.post(refresh_url, json=data)
            if response.status_code == 200:
                new_access_token = response.json().get('access')
                logging.info("Access token refreshed successfully.")
                return new_access_token
            else:
                logging.error(f"Failed to refresh access token: {response.text}")
                return None
        except Exception as e:
            logging.error(f"Error refreshing token: {e}")
            return None
    def validate_token(token):
        # Implement your token validation logic, typically a call to a "validate token" API endpoint
        url = 'http://127.0.0.1:8000/api/validate_token/'
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.get(url, headers=headers)
            return response.status_code == 200
        except requests.RequestException as e:
            logging.error(f"Token validation failed: {e}")
            return False


    def save_session(self, email, password, access_token, refresh_token):
        with open('session.json', 'w') as session_file:
            json.dump({
                'email': email,
                'password': password,
                'access_token': access_token,
                'refresh_token': refresh_token
            }, session_file)
            
    def get_email(self):
        try:
            with open('session.json', 'r') as session_file:
                session_data = json.load(session_file)
            return session_data.get('email')#, session_data.get('refresh')
        except Exception as e:
            return None
    def get_password(self):
        try:
            with open('session.json', 'r') as session_file:
                session_data = json.load(session_file)
            return session_data.get('password')#, session_data.get('refresh')
        except Exception as e:
            return None
    def get_access_token(self):
        try:
            with open('session.json', 'r') as session_file:
                session_data = json.load(session_file)
            return session_data.get('access_token')#, session_data.get('refresh')
        except Exception as e:
            return None
    def get_refresh_token(self):
        try:
            with open('session.json', 'r') as session_file:
                session_data = json.load(session_file)
            return session_data.get('refresh_token')#, session_data.get('refresh')
        except Exception as e:
            return None

