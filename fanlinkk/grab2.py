import requests
import logging
import urllib
from datetime import datetime  # Import this
from PySide6.QtCore import QThread, Signal
from db_utils import get_models_for_user, insert_notification, get_cookies_for_model

# Base URL for the new data requests
base_url = "https://www.fanvue.com/trpc/notifications.getListableNotifications?input="

# Generate inputs with eventType between 7 and 12
inputs = [
    '{"json":{"eventType":9,"cursor":null},"meta":{"values":{"cursor":["undefined"]}}}',
    '{"json":{"eventType":10,"cursor":null},"meta":{"values":{"cursor":["undefined"]}}}',
    '{"json":{"eventType":11,"cursor":null},"meta":{"values":{"cursor":["undefined"]}}}',
]

def urlencoder(base_url, json_input):
    return base_url + urllib.parse.quote(json_input)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate the list of URLs with the specified event types
links = [urlencoder(base_url, input_json) for input_json in inputs]

class DataFetcher(QThread):
    data_fetched = Signal(dict)

    def __init__(self, user_id=None, parent=None):
        super().__init__(parent)
        self.user_id = user_id 

    def run(self):
        logging.info(f"Fetching data for all models for user_id: {self.user_id}...")
        models_data = self.fetch_data_for_all_models()
        self.data_fetched.emit(models_data)
        logging.info("Data fetching completed.")

    def filegrab(self, i, url, cookies, model_email):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "Cookie": f"__Host-next-auth.csrf-token={cookies['csrf_cookies']}; fv-auth.session-token={cookies['auth_token']}"
        }

        session = requests.Session()
        req = requests.Request('GET', url, headers=headers)
        prepared = session.prepare_request(req)
        response = session.send(prepared)

        if response.status_code == 200:
            json_data = response.json()
            self.save_to_db(json_data, model_email)
            logging.info(f"Data successfully written to database for {model_email}")
            return json_data
        else:
            logging.error(f"Failed to retrieve data: {response.status_code}")
            logging.error(f"Response Content: {response.text}")
            return None

    def save_to_db(self, data, model_email):
        # Extract items from the JSON
        items = data.get('result', {}).get('data', {}).get('json', {}).get('items', [])
        for item in items:
            # Extract the necessary fields
            uuid = item.get('uuid')
            created_at_str = item.get('created_at')
            event_type = item.get('event_type')
            price = item.get('data', {}).get('price', 0)
            receiver_uuid = item.get('receiver_uuid')
            model_email = model_email
            # Convert the 'created_at' string to a datetime object
            created_at = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:%S.%fZ')  # Adjust format as needed

            # Insert into the database using db_utils
            try:
                insert_notification(
                    uuid=uuid,
                    created_at=created_at,
                    event_type=event_type,
                    receiver_uuid=receiver_uuid,
                    price=price,
                    model_email=model_email
                )
                logging.info(f"Notification {uuid} inserted into the database.")
            except Exception as e:
                logging.error(f"Failed to insert notification {uuid}: {e}")

    def fetch_data_for_all_models(self):
        # Fetch all models for the user
        models = get_models_for_user(self.user_id)
        models_data = {}

        if models:
            for model in models:
                model_id = model['id']
                model_name = model['name']
                model_email = model['email']           # Fetch cookies for the model using db_utils
                cookies = get_cookies_for_model(model_id)

                if cookies:
                    model_data = {}
                    for i, url in enumerate(links):
                        data = self.filegrab(i, url, cookies, model_email)
                        model_data[f'response_{i}'] = data

                    models_data[model_name] = model_data
                else:
                    logging.warning(f"No cookies found for model {model_name}, skipping data fetch.")
        else:
            logging.warning(f"No models found for user_id: {self.user_id}")
        
        return models_data

# Example Usage:
# fetcher = DataFetcher(user_id=1)  # Replace with the actual user_id
# fetcher.run()
