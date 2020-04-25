

class Node:

    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0
        self.temp = 0
        self.bc = False

    def print_xy(self):
        print("({} , {})".format(round(self.x, 2), round(self.y, 2)), end="", flush=True)
