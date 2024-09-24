import requests
import logging
import token_utils  # Import your token utilities

class DjangoUtils:
    def __init__(self):
        self.token_utils = token_utils.TokenUtils()  # Create an instance of TokenUtils
        self.session = requests.Session()
        self.access_token = self.token_utils.get_access_token()  # Now calling instance method
        self.refresh_token = self.token_utils.get_refresh_token()
    def get_headers(self):
        """Helper function to return headers with JWT access token."""
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'  # Attach access token
        }

    def refresh_access_token(self):
        """Handle token refresh using the utility from token_utils."""
        new_access_token = token_utils.refresh_access_token(self.refresh_token)
        if new_access_token:
            self.access_token = new_access_token  # Update the access token
            return True
        else:
            logging.error("Failed to refresh the access token.")
            return False

    # def get_all_users(self):
    #     url = "http://127.0.0.1:8000/api/users/"
    #     try:
    #         logging.info('Fetching all users...')
    #         response = self.session.get(url, headers=self.get_headers())

    #         if response.status_code == 401:
    #             logging.info("Access token expired, refreshing token...")
    #             if self.refresh_access_token():
    #                 # Retry the request with the new token
    #                 response = self.session.get(url, headers=self.get_headers())
    #             else:
    #                 logging.error("Failed to refresh access token.")
    #                 return []

    #         if response.status_code == 200:
    #             return response.json()
    #         else:
    #             logging.error(f"Error fetching users: {response.status_code}")
    #             return []
    #     except Exception as e:
    #         logging.error(f"Error fetching users: {e}")
    #         return []


    def get_user_organization(self, user_email):
        """
        Fetch the organization ID for the currently authenticated user.
        """
        url = f"http://127.0.0.1:8000/api/organisation/getid/{user_email}/"

        try:
            response = self.session.get(url, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.get(url, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return None

            if response.status_code == 200:
                data = response.json()
                # Use the 'id' field, as returned by the server
                return data.get('id')  # Fetch organization ID
            else:
                logging.error(f"Error fetching organization: {response.status_code}")
                return None
        except Exception as e:
            logging.error(f"Error fetching organization: {e}")
            return None


    def get_models_for_organisation(self, org_id):
        url = f"http://127.0.0.1:8000/api/models/org/{org_id}/"

        try:
            response = self.session.get(url, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.get(url, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return None

            if response.status_code == 200:
                data = response.json()
                if not isinstance(data, list):
                
                    raise ValueError("Expected a list of models but got something else")

                # Use the 'id' field, as returned by the server
                return data.get('id')  # Fetch organization ID
            else:
                logging.error(f"Error fetching organization: {response.status_code}")
                return None
        except Exception as e:
            logging.error(f"Error fetching organization: {e}")
            return None



    def get_all_employees(self, organization_id):
        url = f"http://127.0.0.1:8000/api/organisation/getusers/{organization_id}"
        try:
            logging.info(f'Fetching all users for organization {organization_id}...')
            response = self.session.get(url, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.get(url, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return []

            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Error fetching users: {response.status_code}")
                return []
        except Exception as e:
            logging.error(f"Error fetching users: {e}")
            return []

        

    def get_subordinates_for_supervisor(self, supervisor_email):
        url = f"http://127.0.0.1:8000/api/users/subordinates/{supervisor_email}/"
        try:
            logging.info(f'Fetching subordinates for supervisor: {supervisor_email}')
            response = self.session.get(url, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.get(url, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return []

            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Error fetching subordinates: {response.status_code}")
                return []
        except Exception as e:
            logging.error(f"Error fetching subordinates: {e}")
            return []

    def get_models_for_user(self, user_email):
        url = f"http://127.0.0.1:8000/api/models/user/{user_email}/"
        try:
            logging.info(f'Fetching models for user: {user_email}')
            response = self.session.get(url, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.get(url, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return []

            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Error fetching models: {response.status_code}")
                return []
        except Exception as e:
            logging.error(f"Error fetching models: {e}")
            return []

    def get_employees_for_user(self, user_email):
        url = f"http://127.0.0.1:8000/api/employees/{user_email}/"
        try:
            logging.info(f'Fetching employees for user: {user_email}')
            response = self.session.get(url, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.get(url, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return []

            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Error fetching employees: {response.status_code}")
                return []
        except Exception as e:
            logging.error(f"Error fetching employees: {e}")
            return []

            
    def create_user(self, name, email, role, password):
        """Send a POST request to create a new user."""
        url = "http://127.0.0.1:8000/api/users/"
        data = {
            "name": name,
            "email": email,
            "role": role,
            "password": password  # Default password
        }
        try:
            logging.info(f"Creating user: {name} with email: {email}")
            response = self.session.post(url, json=data, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.post(url, json=data, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return None

            if response.status_code == 201:  # 201 Created
                user_id = response.json().get('id')  # Assuming the response contains the new user ID
                logging.info(f"User {name} created successfully with ID: {user_id}")
                return user_id
            else:
                logging.error(f"Error creating user: {response.text}")
                return None
        except Exception as e:
            logging.error(f"Error creating user: {e}")
            return None
        

    def assign_employee_to_user(self, user_email, employee_email):
        """Send a POST request to assign an employee to a user."""
        url = "http://127.0.0.1:8000/api/users/assign_employees/"
        data = {
            "user_email": user_email,
            "employee_email": employee_email
        }
        try:
            logging.info(f"Assigning employee {employee_email} to user {user_email}")
            response = self.session.post(url, json=data, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.post(url, json=data, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return None

            if response.status_code == 200:  # Success
                logging.info(f"Employee {employee_email} assigned to user {user_email} successfully.")
            else:
                logging.error(f"Error assigning employee: {response.text}")
        except Exception as e:
            logging.error(f"Error assigning employee: {e}")

    def get_user_by_email(self, user_email):
        """Fetch a user by their email."""
        url = f"http://127.0.0.1:8000/api/users/email/{user_email}/"
        try:
            logging.info(f'Fetching user with email: {user_email}')
            response = self.session.get(url, headers=self.get_headers())

            if response.status_code == 401:
                logging.info("Access token expired, refreshing token...")
                if self.refresh_access_token():
                    response = self.session.get(url, headers=self.get_headers())
                else:
                    logging.error("Failed to refresh access token.")
                    return None

            if response.status_code == 200:
                return response.json()  # Return the user data as JSON
            else:
                logging.error(f"Error fetching user: {response.status_code}")
                return None
        except Exception as e:
            logging.error(f"Error fetching user: {e}")
            return None