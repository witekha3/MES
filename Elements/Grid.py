from cmath import sqrt

import numpy as np

from GlobalData import GlobalData


class Grid:
    nodes = []
    elements = []
    global_data = GlobalData()
    global_matrix_C = np.zeros((global_data.n_N, global_data.n_N))
    global_matrix_H = np.zeros((global_data.n_N, global_data.n_N))

    def __init__(self):
        Grid.fill_global_matrix()

    @staticmethod
    def fill_global_matrix():
        for element in Grid.elements:
            for i in range(0, GlobalData().n_W):
                for j in range(0, GlobalData().n_H):
                    Grid.global_matrix_H[element.id_array[i]][element.id_array[j]] += np.round(element.H_matrix[i][j], 6)
                    Grid.global_matrix_C[element.id_array[i]][element.id_array[j]] += np.round(element.C_matrix[i][j], 6)

    @staticmethod
    def print_nodes():
        for node in Grid.nodes:
            node.print_xy()

    @staticmethod
    def print_elements():
        for element in Grid.elements:
            element.print_id_array()

