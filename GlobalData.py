from Tools.FileManager import FileManager


class GlobalData:

    def __init__(self):
        config = FileManager().config_file

        self.H = config["H"]
        self.W = config["W"]
        self.n_H = config["n_H"]
        self.n_W = config["n_H"]
        self.n_N = self.n_H * self.n_W
        self.n_E = (self.n_H - 1) * (self.n_W - 2)
        self.conductivity = config["conductivity"]
        self.amb_temp = config["amb temp"]
        self.init_temp = config["init temp"]
        self.simulation_time = config["sim time"]
        self.simulation_step = config["sim step time"]
        self.alpha = config["alpha"]


