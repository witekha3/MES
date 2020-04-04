from pprint import pprint

import numpy as np


class UniversalElementCalculator:

    def __init__(self, eta_array, ksi_array, x, y):
        self.eta_array = eta_array
        self.ksi_array = ksi_array
        self.x = x
        self.y = y
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
        self.calculate_dNT_dEta()
        self.calculate_dNT_dKsi()
        self.calculate_dXY_dEK()
        self.calculate_det()
        self.calculate_dN_dX()
        self.calculate_integral_points()
        self.calculate_H()


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
        self.H.append(np.round(np.multiply(np.multiply(30, self.det), np.add(self.integral_points_x, self.integral_points_y)),2))


    def calculate_universal_element(self):
        return np.sum(self.H, axis=1)
