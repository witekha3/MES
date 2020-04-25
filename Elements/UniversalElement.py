from cmath import sqrt

from Calculators.UniversalElementCalculator import UniversalElementCalculator


class UniversalElement:

    def __init__(self, x_array, y_array):
        ksi_array = [-1/sqrt(3), 1/sqrt(3), 1/sqrt(3), -1/sqrt(3)]
        eta_array = [-1/sqrt(3), -1/sqrt(3), 1/sqrt(3), 1/sqrt(3)]
        universal_element_calculator = UniversalElementCalculator(eta_array, ksi_array, x_array, y_array)
        self.H_matrices = universal_element_calculator.H_matrics_sum
        self.C_matrices = universal_element_calculator.C_matrics_sum
