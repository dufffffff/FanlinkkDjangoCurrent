import os
import json
import logging
from PySide6.QtCore import QThread, Signal

# Directory containing the JSON files
json_directory = os.path.dirname(os.path.abspath(__file__))

class JSONProcessor(QThread):
    data_processed = Signal(dict)

    def __init__(self, model_name=None):
        super().__init__()
        self.model_data = {}
        self.model_name = model_name  # Use model name instead of email

    def run(self):
        if self.model_name:
            logging.info(f"Processing JSON files for model: {self.model_name}")
            self.search_json_files(json_directory, self.model_name)
        else:
            logging.info("Processing JSON files for all models.")
            self.process_all_models()
        self.emit_processed_data()

    def process_all_models(self):
        for filename in os.listdir(json_directory):
            if filename.endswith('.json'):
                model_name = '_'.join(os.path.splitext(filename)[0].split('_')[:-1])  # Extract the model name from the filename
                logging.info(f"Processing file: {filename} for model: {model_name}")
                self.search_json_files(json_directory, model_name)

    def search_json_files(self, directory, model_name):
        if model_name not in self.model_data:
            self.model_data[model_name] = {}

        for filename in os.listdir(directory):
            if filename.startswith(model_name) and filename.endswith('.json'):
                file_path = os.path.join(directory, filename)
                key_from_filename = os.path.splitext(filename)[0].split('_')[-1]
                logging.info(f"Reading file: {file_path}")
                with open(file_path, 'r') as json_file:
                    try:
                        data = json.load(json_file)
                        if 'result' not in data or 'data' not in data['result'] or 'json' not in data['result']['data']:
                            logging.error(f"Unexpected JSON structure in {file_path}")
                            continue

                        json_content = data['result']['data']['json']
                        if isinstance(json_content, dict):
                            self.process_json_content(json_content, model_name)
                        elif isinstance(json_content, list):
                            self.model_data[model_name][key_from_filename] = json_content
                        else:
                            self.model_data[model_name][key_from_filename] = data

                        logging.info(f"Successfully processed data for {model_name} from file: {filename}")
                    except json.JSONDecodeError as e:
                        logging.error(f"Error decoding JSON from file {file_path}: {e}")

    def process_json_content(self, json_content, model_name):
        # Normalize the model name at the beginning
        normalized_model_name = model_name.replace('_response', '').lower()

        if normalized_model_name not in self.model_data:
            self.model_data[normalized_model_name] = {}

        metrics = {
            'tips': json_content.get('tips', {}).get('currentPeriodGross', 0),
            'subs': json_content.get('subscriptions', {}).get('currentPeriodGross', 0),
            'ptv': json_content.get('payToView', {}).get('currentPeriodGross', 0),
            'renewals': json_content.get('renewals', {}).get('currentPeriodGross', 0),
            'messages': sum(entry.get('gross', 0) for entry in json_content.get('currentPeriod', []))
        }

        for key, value in metrics.items():
            if key in self.model_data[normalized_model_name]:
                self.model_data[normalized_model_name][key] += value
            else:
                self.model_data[normalized_model_name][key] = value


    def calculate_total_for_metric(self, model_name, metric_type):
        """Calculate total value for a specific metric type for a single model."""
        return self.model_data.get(model_name, {}).get(metric_type, 0)
    
    def get_metrics_for_model(self, model_name):
        """Fetch tips, subs, ptv, renewals, and messages for a specific model."""
        logging.info(f"Attempting to retrieve metrics for model: {model_name}")
        
        # Normalize the model name to ensure consistency
        normalized_model_name = model_name.lower().replace(" ", "_")
        logging.info(f"Normalized model name: {normalized_model_name}")
        
        if normalized_model_name not in self.model_data:
            logging.error(f"Model data for {normalized_model_name} not found in JSONProcessor.")
            return None
        
        metrics = {
            'tips': self.calculate_total_for_metric(normalized_model_name, 'tips'),
            'subs': self.calculate_total_for_metric(normalized_model_name, 'subs'),
            'ptv': self.calculate_total_for_metric(normalized_model_name, 'ptv'),
            'renewals': self.calculate_total_for_metric(normalized_model_name, 'renewals'),
            'messages': self.calculate_total_for_metric(normalized_model_name, 'messages')
        }
        logging.info(f"Metrics for {normalized_model_name}: {metrics}")
        return metrics
    
    def emit_processed_data(self):
        # Emit processed data for all models using normalized names
        all_metrics = {}
        for model_name in self.model_data.keys():
            all_metrics[model_name] = self.get_metrics_for_model(model_name)
        logging.info(f"Emitting processed data for all models: {all_metrics}")
        self.data_processed.emit(all_metrics)

