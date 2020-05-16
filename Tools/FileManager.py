import json
from pathlib import Path

import numpy as np


class FileManager:

    def __init__(self):
        self.root_dir = self.config_file = Path(__file__).parent.parent
        self.config_file = self.load_config_file()

    def load_config_file(self):
        with open(str(self.root_dir) + r"\Files\config.json") as f:
            data = json.load(f)
        return data

    def load_result_to_compare(self):
        with open(str(self.root_dir) + r"\Files\result_to_compare.txt") as f:
            data = np.loadtxt(f, delimiter=" ")
        return data

