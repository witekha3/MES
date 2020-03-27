from array import *
from cmath import sqrt
from pprint import pprint

import numpy as np


def calculate_dNT_eta_row(eta):
    dN1 = round((-0.25 *(1-eta)).real, 5)
    dN2 = round((0.25 * (1-eta)).real, 5)
    dN3 = round((0.25 * (1+eta)).real, 5)
    dN4 = round((-0.25 * (1+eta)).real, 5)


    return [dN1, dN2, dN3, dN4]

def calculate_dNT_ksi_row(eta):
    dN1 = round((-0.25 *(1-eta)).real, 5)
    dN2 = round((-0.25 * (1+eta)).real, 5)
    dN3 = round((0.25 * (1+eta)).real, 5)
    dN4 = round((0.25 * (1-eta)).real, 5)

    return [dN1, dN2, dN3, dN4]


def calculate_dXY(tab, dNT):
    tmp = list()
    d=0
    for i in range(0,len(tab)):
        d += dNT[i] * tab[i]
    return d

def calculate_det(row1, row2):
    return  round((row1[0] * row2[1] - row1[1] * row2[1]).real, 8)


def matmult(a,b, c, det):
    return np.dot(np.dot(1/det, [a,b]), c)


if __name__ == "__main__":

    ksi1 = -(1/sqrt(3))
    eta1 = -(1/sqrt(3))

    ksi2 = (1/sqrt(3))
    eta2 = -(1/sqrt(3))

    ksi3 = (1/sqrt(3))
    eta3 = (1/sqrt(3))

    ksi4 = -(1/sqrt(3))
    eta4 = (1/sqrt(3))

    xT = [0, 0.025, 0.025, 0]
    yT = [0, 0, 0.025, 0.025]

    dNT_eta = [calculate_dNT_eta_row(eta1), calculate_dNT_eta_row(eta2), calculate_dNT_eta_row(eta3), calculate_dNT_eta_row(eta4)]
    dNT_ksi = [calculate_dNT_ksi_row(ksi1), calculate_dNT_ksi_row(ksi2), calculate_dNT_ksi_row(ksi3),calculate_dNT_ksi_row(ksi4)]

    det = list()
    det.append(calculate_det([calculate_dXY(xT, dNT_eta[0]), calculate_dXY(yT, dNT_eta[0])],
                        [calculate_dXY(xT, dNT_ksi[0]), calculate_dXY(yT, dNT_ksi[0])]))
    det.append(calculate_det([calculate_dXY(xT, dNT_eta[1]), calculate_dXY(yT, dNT_eta[1])],
                        [calculate_dXY(xT, dNT_ksi[1]), calculate_dXY(yT, dNT_ksi[1])]))
    det.append(calculate_det([calculate_dXY(xT, dNT_eta[2]), calculate_dXY(yT, dNT_eta[2])],
                        [calculate_dXY(xT, dNT_ksi[2]), calculate_dXY(yT, dNT_ksi[2])]))
    det.append(calculate_det([calculate_dXY(xT, dNT_eta[3]), calculate_dXY(yT, dNT_eta[3])],
                        [calculate_dXY(xT, dNT_ksi[3]), calculate_dXY(yT, dNT_ksi[3])]))

    a = matmult([calculate_dXY(yT, dNT_ksi[0]), -1*calculate_dXY(yT, dNT_eta[0])],
             [-1*calculate_dXY(xT, dNT_ksi[0]), calculate_dXY(xT, dNT_eta[0])], [dNT_eta[0], dNT_ksi[0]], det[0])



