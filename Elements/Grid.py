from cmath import sqrt

import numpy as np

from GlobalData import GlobalData


class Grid:
    nodes = []
    elements = []
    global_data = GlobalData()
    global_matrix_C = np.zeros((global_data.n_N, global_data.n_N))
    global_matrix_H = np.zeros((global_data.n_N, global_data.n_N))
    global_vector_P = np.zeros((global_data.n_N, 1))

    def __init__(self):
        Grid.fill_global_matrix()

    @staticmethod
    def fill_global_matrix():
        for element in Grid.elements:
            Grid.global_vector_P[element.id_array] += element.P_vector
            for i in range(0, 4):
                for j in range(0, 4):
                    Grid.global_matrix_H[element.id_array[i]][element.id_array[j]] += element.H_matrix[i][j]
                    Grid.global_matrix_C[element.id_array[i]][element.id_array[j]] += element.C_matrix[i][j]

    @staticmethod
    def print_nodes():
        for node in Grid.nodes:
            node.print_xy()

    @staticmethod
    def print_elements():
        for element in Grid.elements:
            element.print_id_array()

