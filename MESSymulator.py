from pprint import pprint
import scipy.linalg as la
import numpy as np
import scipy

from Creator import Creator
from Elements.Grid import Grid
from GlobalData import GlobalData
from Tools.FileManager import FileManager


class MESSymulator:
    def __init__(self):
        Creator().create_nodes_for_grid()
        Creator().create_elements_for_grid()
        grid = Grid()
        global_data = GlobalData()
        self.H_matrix = grid.global_matrix_H
        self.C_matrix = grid.global_matrix_C
        self.P_vector = grid.global_vector_P
        self.init_temp = global_data.init_temp
        self.simulation_time = global_data.simulation_time
        self.simulation_step = global_data.simulation_step



    def start(self):
        t0 = np.full((len(self.H_matrix), 1), self.init_temp)
        step_temp_dict = {}
        print("Time[s] \t MaxTemps[s] \t MinTemps[s]")
        for i in range(self.simulation_step, self.simulation_time + self.simulation_step, self.simulation_step):
            p = np.dot((self.C_matrix / self.simulation_step), t0) + self.P_vector
            h = self.H_matrix + (self.C_matrix / self.simulation_step)
            t0 = np.linalg.solve(h, p)
            step_temp_dict[i] = {}
            step_temp_dict[i]["min"] = np.min(t0)
            step_temp_dict[i]["max"] = np.max(t0)
        pprint(step_temp_dict)
