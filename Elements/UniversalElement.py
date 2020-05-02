from cmath import sqrt
from pprint import pprint

from Calculators.UniversalElementCalculator import UniversalElementCalculator
from Calculators.VectorPCalculator import VectorPCalculator
from GlobalData import GlobalData


class UniversalElement:

    def __init__(self, x_array, y_array):
        ksi_array = [-1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3), -1 / sqrt(3)]
        eta_array = [-1 / sqrt(3), -1 / sqrt(3), 1 / sqrt(3), 1 / sqrt(3)]
        self.N_array = [[0, 0.025, 0.025, 0], [0, 0, 0.025, 0.025]]
        universal_element_calculator = UniversalElementCalculator(eta_array, ksi_array, x_array, y_array)
        self.H_matrices = universal_element_calculator.get_H_sum_matrix()
        self.C_matrices = universal_element_calculator.get_C_sum_matrix()
        vector_p_calculatpr = VectorPCalculator(self.N_array).calculate_H_bc()
