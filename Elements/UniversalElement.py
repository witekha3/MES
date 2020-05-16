from cmath import sqrt
from pprint import pprint

import numpy as np

from Calculators.UniversalElementCalculator import UniversalElementCalculator
from Calculators.BorderCalculator import BorderCalculator
from GlobalData import GlobalData


class UniversalElement:

    def __init__(self, x_array, y_array, bc_nodes_array):
        ksi_array = [-1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3), -1 / sqrt(3)]
        eta_array = [-1 / sqrt(3), -1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3)]
        self.N_array = [x_array, y_array]
        universal_element_calculator = UniversalElementCalculator(eta_array, ksi_array, x_array, y_array)
        self.H_matrix = np.array(universal_element_calculator.get_H_sum_matrix())
        self.C_matrix = universal_element_calculator.get_C_sum_matrix()
        self.P_vector = np.zeros((4, 1))
        self.add_H_bc_and_P_vector(bc_nodes_array)
        X=2

    def add_H_bc_and_P_vector(self, bc_nodes_array):
        # 0-bottom, 1-right, 2-top, 3-left
        def add(id):
            border_calculator = BorderCalculator(self.N_array)
            H_bc = border_calculator.calculate_H_bc()[id]
            self.P_vector = np.add(self.P_vector, border_calculator.calculate_P_vector()[id])
            self.H_matrix = np.add(self.H_matrix, H_bc)

        if bc_nodes_array[0] and bc_nodes_array[1]:
            add(0)
        if bc_nodes_array[1] and bc_nodes_array[2]:
            add(1)
        if bc_nodes_array[2] and bc_nodes_array[3]:
            add(2)
        if bc_nodes_array[0] and bc_nodes_array[3]:
            add(3)


