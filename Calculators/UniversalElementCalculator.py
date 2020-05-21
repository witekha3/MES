import itertools
import numpy as np

from Calculators.JakobianCalculator import JakobianCalculator
from GlobalData import GlobalData
from Tools.FileManager import FileManager


class UniversalElementCalculator(JakobianCalculator):

    def __init__(self, eta_array, ksi_array, x, y):
        super().__init__(eta_array, ksi_array, x, y)
        global_data = GlobalData()
        self.eta_array = eta_array
        self.ksi_array = ksi_array
        self.cp = global_data.cp
        self.ro = global_data.density
        self.N = []
        self.integral_points_x = []
        self.integral_points_y = []
        self.H = []
        self.C = []
        self.H_matrics_sum = []
        self.C_matrics_sum = []
        self.make_main_calculations()

    def make_main_calculations(self):
        self.calculate_jakobian()
        self.calculate_N()
        self.calculate_integral_points()

    def get_H_sum_matrix(self):
        self.calculate_H()
        self.calculate_H_matrics_sum()
        return self.H_matrics_sum

    def get_C_sum_matrix(self):
        self.calculate_C()
        self.calculate_C_matrics_sum()
        return self.C_matrics_sum

    def calculate_N(self):
        N1_array = []
        N2_array = []
        N3_array = []
        N4_array = []

        for ksi, eta in zip(self.ksi_array, self.eta_array):
            N1_array.append((0.25 * ((1 - ksi) * (1 - eta))).real)
            N2_array.append((0.25 * ((1 + ksi) * (1 - eta))).real)
            N3_array.append((0.25 * ((1 + ksi) * (1 + eta))).real)
            N4_array.append((0.25 * ((1 - ksi) * (1 + eta))).real)

        self.N.append(N1_array)
        self.N.append(N2_array)
        self.N.append(N3_array)
        self.N.append(N4_array)

    def calculate_integral_points(self):
        for i in range(0, len(self.dN_dx)):
            self.integral_points_x.append(np.dot(self.dN_dx[i].reshape(4, 1), [self.dN_dx[i]]))
            self.integral_points_y.append(np.dot(self.dN_dy[i].reshape(4, 1), [self.dN_dy[i]]))

    def calculate_H(self):
        self.H.append(np.multiply(np.multiply(GlobalData().conductivity, self.det),
                                  np.add(self.integral_points_x, self.integral_points_y)))

    def calculate_H_matrics_sum(self):
        self.H_matrics_sum = np.sum(self.H, axis=1)
        self.H_matrics_sum = list(itertools.chain.from_iterable(self.H_matrics_sum))

    def calculate_C(self):
        cp_x_ro = self.cp * self.ro
        for N in self.N:
            N = np.array(N)
            Nt_x_N = np.multiply(np.array(N).reshape(4, 1), N)
            self.C.append(np.multiply(np.dot(cp_x_ro, Nt_x_N), self.det))

    def calculate_C_matrics_sum(self):
        self.C_matrics_sum = np.sum(self.C, axis=0)
