import json
from pathlib import Path
class FileManager:

    def __init__(self):
        self.root_dir = self.config_file = Path(__file__).parent.parent
        self.config_file = self.load_config_file()

    def load_config_file(self):
        with open(str(self.root_dir) + "\Files\config.json") as f:
            data = json.load(f)
        return data

