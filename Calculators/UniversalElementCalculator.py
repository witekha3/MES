import itertools
import numpy as np

from GlobalData import GlobalData
from Tools.FileManager import FileManager


class UniversalElementCalculator:

    def __init__(self, eta_array, ksi_array, x, y):
        file_manager = FileManager()
        self.eta_array = eta_array
        self.ksi_array = ksi_array
        self.x = x
        self.y = y
        self.cp = file_manager.config_file["spec heat"]
        self.ro = file_manager.config_file["density"]
        self.N = []
        self.dN_dEta = []
        self.dN_dKsi = []
        self.dx_dEta = []
        self.dx_dKsi = []
        self.dy_dEta = []
        self.dy_dKsi = []
        self.det = []
        self.dN_dx = []
        self.dN_dy = []
        self.integral_points_x = []
        self.integral_points_y = []
        self.H = []
        self.C = []
        self.H_matrics_sum = []
        self.C_matrics_sum = []
        self.make_main_calculations()


    def make_main_calculations(self):
        self.calculate_N()
        self.calculate_dNT_dEta()
        self.calculate_dNT_dKsi()
        self.calculate_dXY_dEK()
        self.calculate_det()
        self.calculate_dN_dX()
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
            N1_array.append(round((0.25 * ((1 - ksi) * (1 - eta))).real, 5))
            N2_array.append(round((0.25 * ((1 + ksi) * (1 - eta))).real, 5))
            N3_array.append(round((0.25 * ((1 + ksi) * (1 + eta))).real, 5))
            N4_array.append(round((0.25 * ((1 - ksi) * (1 + eta))).real, 5))

        self.N.append(N1_array)
        self.N.append(N2_array)
        self.N.append(N3_array)
        self.N.append(N4_array)

    def calculate_dNT_dEta(self):
        for ksi in self.ksi_array:
            dN1 = round((-0.25 * (1 - ksi)).real, 6)
            dN2 = round((-0.25 * (1 + ksi)).real, 6)
            dN3 = round((0.25 * (1 + ksi)).real, 6)
            dN4 = round((0.25 * (1 - ksi)).real, 6)
            self.dN_dEta.append([dN1, dN2, dN3, dN4])

    def calculate_dNT_dKsi(self):
        for eta in self.eta_array:
            dN1 = round((-0.25 * (1 - eta)).real, 6)
            dN2 = round((0.25 * (1 - eta)).real, 6)
            dN3 = round((0.25 * (1 + eta)).real, 6)
            dN4 = round((-0.25 * (1 + eta)).real, 6)
            self.dN_dKsi.append([dN1, dN2, dN3, dN4])

    def calculate_dXY_dEK(self):
        for dN_dEta, dN_dKsi in zip(self.dN_dEta, self.dN_dKsi):
            dx_eta = 0
            dx_ksi = 0
            dy_eta = 0
            dy_ksi = 0
            for i in range(0, len(dN_dEta)):
                dx_eta += dN_dEta[i] * self.x[i]
                dx_ksi += dN_dKsi[i] * self.x[i]
                dy_eta += dN_dEta[i] * self.y[i]
                dy_ksi += dN_dKsi[i] * self.y[i]
            self.dx_dEta.append([dx_eta])
            self.dx_dKsi.append([dx_ksi])
            self.dy_dEta.append([dy_eta])
            self.dy_dKsi.append([dy_ksi])


    def calculate_det(self):
        for dx_dKsi, dy_dKsi, dx_dEta, dy_dEta in zip(self.dx_dKsi, self.dy_dKsi, self.dx_dEta, self.dy_dEta):
            self.det.append([round((dx_dKsi[0] * dy_dEta[0] - dy_dKsi[0] * dx_dEta[0]).real, 8)])

    def calculate_dN_dX(self):
        for dx_dKsi, dy_dKsi, dx_dEta, dy_dEta, det, i in \
                zip(self.dx_dKsi, self.dy_dKsi, self.dx_dEta, self.dy_dEta, self.det, range(0, len(self.dN_dEta))):
            dN_dx, dN_dy = np.dot(np.dot(1 / det[0], [[dy_dEta[0], -dy_dKsi[0]], [-dx_dEta[0], dx_dKsi[0]]]), [self.dN_dKsi[i], self.dN_dEta[i]])
            self.dN_dx.append(dN_dx)
            self.dN_dy.append(dN_dy)

    def calculate_integral_points(self):
        for i in range(0, len(self.dN_dx)):
            self.integral_points_x.append(np.round(np.dot(self.dN_dx[i].reshape(4,1), [self.dN_dx[i]]),2))
            self.integral_points_y.append(np.round(np.dot(self.dN_dy[i].reshape(4,1), [self.dN_dy[i]]),2))

    def calculate_H(self):
        self.H.append(np.round(np.multiply(np.multiply(GlobalData().conductivity, self.det),
                                           np.add(self.integral_points_x, self.integral_points_y)),2))


    def calculate_H_matrics_sum(self):
        self.H_matrics_sum = np.sum(self.H, axis=1)
        self.H_matrics_sum = list(itertools.chain.from_iterable(self.H_matrics_sum))

    def calculate_C(self):
        cp_x_ro = self.cp * self.ro
        for N in self.N:
            Nt = np.array(N).reshape(4, 1)
            N = np.array(N)
            Nt_x_N = np.multiply(Nt, N)
            self.C.append(np.multiply(np.dot(cp_x_ro, Nt_x_N), self.det))

    def calculate_C_matrics_sum(self):
        self.C_matrics_sum = np.round(np.sum(self.C, axis=0), 4)




