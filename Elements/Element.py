from pprint import pprint

import numpy as np


class Element:

    def __init__(self):
        self.id_array = []
        self.H_matrix = []
        self.C_matrix = []

    def print_id_array(self):
        pprint(self.id_array[1].print_xy(), self.id_array[2].print_xy())
        pprint(self.id_array[0].print_xy(), self.id_array[3].print_xy())
        print("\n")
