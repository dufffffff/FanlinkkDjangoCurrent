from PySide6.QtCore import QObject, QThread, Signal
from collections import defaultdict
import os
import json, logging

class GrapherWorker(QObject):
    graph_updated = Signal(dict)
    finished = Signal()

    def __init__(self, directory):
        super().__init__()
        self.directory = directory

    def run(self):
        logging.info("GrapherWorker started processing.")
        aggregated_data = self.load_and_aggregate_json_files(self.directory)
        logging.info(f"Aggregated data ready: {aggregated_data}")
        self.graph_updated.emit(aggregated_data)
        self.finished.emit()

    def load_and_aggregate_json_files(self, directory):
        aggregated_data = defaultdict(float)
        for filename in os.listdir(directory):
            if filename.endswith('response_1.json'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as file:
                    data = json.load(file)
                    if 'result' in data and 'data' in data['result'] and 'json' in data['result']['data']:
                        for period in data['result']['data']['json']['currentPeriod']:
                            date = period['date'].split('T')[0]  # Extract just the date part
                            gross = period['gross']
                            aggregated_data[date] += gross
        return aggregated_data

