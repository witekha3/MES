from cmath import sqrt
from pprint import pprint

import numpy as np

from Calculators.UniversalElementCalculator import UniversalElementCalculator
from Calculators.VectorPCalculator import VectorPCalculator
from GlobalData import GlobalData


class UniversalElement:

    def __init__(self, x_array, y_array, bc_nodes_array):
        ksi_array = [-1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3), -1 / sqrt(3)]
        eta_array = [-1 / sqrt(3), -1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3)]
        self.N_array = [x_array, y_array]
        universal_element_calculator = UniversalElementCalculator(eta_array, ksi_array, x_array, y_array)
        self.H_matrix = np.array(universal_element_calculator.get_H_sum_matrix())
        self.C_matrix = universal_element_calculator.get_C_sum_matrix()
        self.add_P_vector(bc_nodes_array)

    def add_P_vector(self, bc_nodes_array):
        if (bc_nodes_array[2] == bc_nodes_array[3]) is True:
            # dodaj bc gorna
            H_bc = np.round(VectorPCalculator(self.N_array).calculate_H_bc()[2], 6)
            self.H_matrix = np.round(np.add(self.H_matrix, H_bc), 6)
        if (bc_nodes_array[0] == bc_nodes_array[1]) is True:
            # dodaj bc dolna
            H_bc = np.round(VectorPCalculator(self.N_array).calculate_H_bc()[0], 6)
            self.H_matrix = np.round(np.add(self.H_matrix, H_bc), 6)
        if (bc_nodes_array[0] == bc_nodes_array[3]) is True:
            # dodaj lewy
            H_bc = np.round(VectorPCalculator(self.N_array).calculate_H_bc()[3], 6)
            self.H_matrix = np.round(np.add(self.H_matrix, H_bc), 6)
        if (bc_nodes_array[1] == bc_nodes_array[2]) is True:
            # dodaj prawy
            H_bc = np.round(VectorPCalculator(self.N_array).calculate_H_bc()[1], 6)
            self.H_matrix = np.round(np.add(self.H_matrix, H_bc), 6)
        X=2



