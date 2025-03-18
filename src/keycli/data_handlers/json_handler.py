import json
from .base_handler import BaseHandler

class JSONHandler(BaseHandler):
    def load_data(self):
        with self.file_path.open() as f:
            return json.load(f)

    def save_data(self, data):
        with self.file_path.open("w") as f:
            json.dump(data, f, indent=4)
