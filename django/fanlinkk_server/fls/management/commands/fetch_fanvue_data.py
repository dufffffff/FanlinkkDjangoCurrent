# fetch_fanvue_data.py

from django.core.management.base import BaseCommand
# Remove the following import, as we'll use timezone from datetime
# from django.utils import timezone
from fls.models import Model, Notification, User
import requests
import logging
import urllib
from datetime import datetime, timedelta, timezone  # Import timezone from datetime

class Command(BaseCommand):
    help = 'Fetch data from Fanvue API and save to the database'

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Starting to fetch data from Fanvue API.")
        self.fetch_data_for_all_models()
        logging.info("Data fetching completed.")

    def fetch_data_for_all_models(self):
        # Use datetime.now(timezone.utc) to get the current UTC time
        active_threshold = datetime.now(timezone.utc) - timedelta(minutes=1)
        active_users = User.objects.filter(last_activity__gte=active_threshold)
        active_models = Model.objects.select_related('user').filter(user__last_activity__gte=active_threshold)

        if not active_models.exists():
            logging.info("No active models found. Exiting data fetch.")
            return

        for model in active_models:
            # Proceed to fetch data for this model
            self.fetch_data_for_model(model)

    def fetch_data_for_model(self, model):
        # Extract cookies and model email
        cookies = {
            'csrf_cookies': model.csrf_cookies,
            'auth_token': model.auth_token,
        }
        model_email = model.email

        # Fetch data from the API for this model
        data = self.fetch_data_from_api(cookies, model_email)
        if data:
            # Save the data to the database
            self.save_data_to_db(data, model_email)
            logging.info(f"Data fetched and saved for model: {model_email}")
        else:
            logging.error(f"Failed to fetch data for model: {model_email}")

    def fetch_data_from_api(self, cookies, model_email):
        base_url = "https://www.fanvue.com/trpc/notifications.getListableNotifications?input="
        inputs = [
            '{"json":{"eventType":9,"cursor":null},"meta":{"values":{"cursor":["undefined"]}}}',
            '{"json":{"eventType":10,"cursor":null},"meta":{"values":{"cursor":["undefined"]}}}',
            '{"json":{"eventType":11,"cursor":null},"meta":{"values":{"cursor":["undefined"]}}}',
        ]

        def urlencoder(base_url, json_input):
            return base_url + urllib.parse.quote(json_input)

        links = [urlencoder(base_url, input_json) for input_json in inputs]
        data = []
        for url in links:
            response = self.api_request(url, cookies)
            if response:
                data.append(response)
            else:
                logging.error(f"Failed to get response from URL: {url}")
        return data if data else None

    def api_request(self, url, cookies):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": "Mozilla/5.0",
            "Cookie": f"__Host-next-auth.csrf-token={cookies['csrf_cookies']}; fv-auth.session-token={cookies['auth_token']}"
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"API request failed: {e}")
            return None

    def save_data_to_db(self, data_list, model_email):
        for data in data_list:
            items = data.get('result', {}).get('data', {}).get('json', {}).get('items', [])
            for item in items:
                uuid = item.get('uuid')
                created_at_str = item.get('created_at')
                event_type = item.get('event_type')
                price = item.get('data', {}).get('price', 0)
                receiver_uuid = item.get('receiver_uuid')

                # Determine purchase_type
                data_field = item.get('data', {})
                if 'post_uuid' in data_field:
                    purchase_type = 'post'
                elif 'route_uuid' in data_field:
                    purchase_type = 'message'
                else:
                    purchase_type = None
                    logging.warning(f"Notification {uuid} has no post_uuid or route_uuid in data field.")

                # Convert the 'created_at' string to a datetime object
                try:
                    created_at = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                except ValueError:
                    created_at = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:%SZ')

                # Make the datetime object timezone-aware (assuming UTC)
                created_at = created_at.replace(tzinfo=timezone.utc)

                # Debug statement to confirm timezone
                logging.debug(f"created_at: {created_at}, tzinfo: {created_at.tzinfo}")

                # Create or update the Notification object
                notification, created = Notification.objects.update_or_create(
                    uuid=uuid,
                    defaults={
                        'created_at': created_at,
                        'event_type': event_type,
                        'receiver_uuid': receiver_uuid,
                        'price': price,
                        'model_email': model_email,
                        'purchase_type': purchase_type,
                    }
                )
                if created:
                    logging.info(f"Notification {uuid} created with purchase_type '{purchase_type}'.")
                else:
                    logging.info(f"Notification {uuid} updated with purchase_type '{purchase_type}'.")
