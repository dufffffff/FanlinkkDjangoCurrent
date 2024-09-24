import db_utils
import requests
import json
import logging
import urllib
from PySide6.QtCore import QThread, Signal, QTimer

# URLs and inputs for the data requests
base_url_1 = "https://www.fanvue.com/trpc/insights.overview?input="
base_url_2 = "https://www.fanvue.com/trpc/insights.earningsChart?input="
base_url_3 = "https://www.fanvue.com/trpc/insights.getSubscribersCountryStats?input="
base_url_4 = "https://www.fanvue.com/trpc/insights.topSellingPosts?input="
base_url_5 = "https://www.fanvue.com/trpc/insights.topSellingMessages?input="
base_url_6 = "https://www.fanvue.com/trpc/insights.topSpenders?input="

input_1 = '{"json":{"period":"ALL","clientStartDate":"2024-08-09T23:00:00.000Z","clientEndDate":null},"meta":{"values":{"clientEndDate":["undefined"]}}}'
input_2 = '{"json":{"type_id":null,"period":"ALL","clientStartDate":"2024-02-10T00:00:00.000+00:00","clientEndDate":"2024-08-11T00:00:00.000+01:00"},"meta":{"values":{"type_id":["undefined"]}}}'
input_3 = '{"json":null,"meta":{"values":["undefined"]}}'

def urlencoder(base_url, json_input):
    return base_url + urllib.parse.quote(json_input)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

links = [
    urlencoder(base_url_1, input_1),
    urlencoder(base_url_2, input_2),
    urlencoder(base_url_3, input_3),
    urlencoder(base_url_4, input_3),
    urlencoder(base_url_5, input_3),
    urlencoder(base_url_6, input_3),
]

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

    def filegrab(self, i, url, cookies, model_name):
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

        # Sanitize model_name to be filesystem-safe (optional, depending on your requirements)
        sanitized_model_name = model_name.replace(' ', '_').replace('.', '_').lower()
        filename = f"./{sanitized_model_name}_response_{i}.json"

        if response.status_code == 200:
            with open(filename, 'w') as json_file:
                json.dump(response.json(), json_file, indent=4)
            logging.info(f"Response has been written to {filename}")
            return response.json()
        else:
            logging.error(f"Failed to retrieve data: {response.status_code}")
            logging.error(f"Response Content: {response.text}")
            return None

    def fetch_data_for_all_models(self):
        models_data = {}
        if self.user_id is None:
            logging.error("User ID is not set!")
            return models_data

        models = db_utils.get_models_for_user(user_id=self.user_id)

        for model in models:
            model_id = model['id']
            model_name = model['name']
            cookies = db_utils.get_cookies_for_model(model_id)

            if cookies:
                model_data = {}
                for i, url in enumerate(links):
                    data = self.filegrab(i, url, cookies, model_name)  # Pass the model name explicitly
                    model_data[f'response_{i}'] = data
                
                models_data[model_name] = model_data
            else:
                logging.warning(f"No cookies found for model {model_name}, skipping data fetch.")

        return models_data
