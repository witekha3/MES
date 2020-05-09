from cmath import sqrt
from pprint import pprint

import numpy as np

from Calculators.UniversalElementCalculator import UniversalElementCalculator
from GlobalData import GlobalData


class VectorPCalculator:
    def __init__(self, N_array, weight=None):
        if weight is None:
            weight = [1, 1]
        self.border_ksi_array = [[-1 / sqrt(3), 1 / sqrt(3)], [1, 1], [1 / sqrt(3), -1 / sqrt(3)], [-1, -1]]
        self.border_eta_array = [[-1, -1], [-1 / sqrt(3), 1 / sqrt(3)], [1, 1], [1 / sqrt(3), -1 / sqrt(3)]]
        self.conductivity = GlobalData().conductivity
        self.N_array = N_array
        self.weight = weight
        self.N = self.calculate_border_N()
        self.jakobies = self.calculate_jakob()
        self.H_bc = []

    def calculate_border_N(self):
        N = []
        for border_eta, border_ksi in zip(self.border_eta_array, self.border_ksi_array):
            N.append(UniversalElementCalculator(border_eta, border_ksi, self.N_array[0], self.N_array[1]).N)
        return N

    def calculate_jakob(self):
        jakob = []
        for i in range(0, len(self.N_array[0]), 2):
            length_bot_top = sqrt(pow((self.N_array[0][i + 1] - self.N_array[0][i]), 2) -
                                  pow((self.N_array[1][i + 1] - self.N_array[1][i]), 2))
            length_left_right = sqrt(pow((self.N_array[1][i + 1] - self.N_array[1][i]), 2) -
                                     pow((self.N_array[0][i + 1] - self.N_array[0][i]), 2))
            jakob.append(length_bot_top / 2)
            jakob.append(length_left_right / 2)
        return jakob

    def calculate_H_bc(self):
        H1 = []
        H2 = []
        for j in range(0, len(self.N)):
            pc1 = []
            pc2 = []
            for i in range(0, len(self.N[j])):
                pc1.append(self.N[j][i][0])
                pc2.append(self.N[j][i][1])
            H1.append(np.multiply(self.conductivity * self.weight[0], np.multiply(np.array(pc1).reshape(4, 1), pc1)))
            H2.append(np.multiply(self.conductivity * self.weight[1], np.multiply(np.array(pc2).reshape(4, 1), pc2)))
        self.H_bc = np.round(np.multiply(np.add(H1, H2), self.jakobies[0]).real, 6)
        return self.H_bc
