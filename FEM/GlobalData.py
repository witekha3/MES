from FileManager import FileManager


class GlobalData:

    def __init__(self):
        init_data = FileManager().load_grid_file("initial_data.json")

        self.H = init_data["H"]
        self.W = init_data["W"]
        self.n_H = init_data["n_H"]
        self.n_W = init_data["n_H"]
        self.n_N = self.n_H * self.n_W
        self.n_E = (self.n_H - 1) * (self.n_W - 2)

