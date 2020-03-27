import json
import os

class FileManager:

    def __int__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

    def load_grid_file(self, name):
        with open(name) as f:
            data = json.load(f)
        return data

