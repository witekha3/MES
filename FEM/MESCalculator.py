from copy import copy
from pprint import pprint

from Element import Element
from Grid import Grid
from Node import Node
from GlobalData import GlobalData
from Printer import Printer


class MESCalculaotr:

    def __init__(self):
        self.H = GlobalData().H
        self.W = GlobalData().W
        self.n_H = GlobalData().n_H
        self.n_W = GlobalData().n_W
        self.lx = self.W/(self.n_W-1)
        self.ly = self.H/(self.n_H-1)

        self.node = Node()
        self.grid = Grid()
        self.element = Element()

        self.printer = Printer()


    def generate_nodes(self):
        for i in range(0, self.n_H):
            for j in range(0, self.n_W):
                self.node.x = i * self.lx
                self.node.y = j * self.ly
                self.grid.nodes.append(copy(self.node))

        self.printer.print_grid(self.grid, self.n_H)





    def generete_elements(self):
        t = []
        counter = 0
        for i in range(0, len(self.grid.nodes)):
            try:
                counter += 1
                if counter == (self.n_H -1):
                    counter = 0
                    continue
                t.append(self.grid.nodes[i])
                t.append(self.grid.nodes[i+4])
                t.append(self.grid.nodes[i+5])
                t.append(self.grid.nodes[i+1])
                self.grid.elements.append(copy(t))

                t.clear()
            except IndexError:
                continue
        #
        # print(self.grid.elements[0][3].x, self.grid.elements[0][3].y)
        # print(self.grid.elements[0][2].x, self.grid.elements[0][2].y)
        # print(self.grid.elements[0][1].x, self.grid.elements[0][1].y)
        # print(self.grid.elements[0][0].x, self.grid.elements[0][0].y)
        # print("\n")
        # print(self.grid.elements[7][3].x, self.grid.elements[7][3].y)
        # print(self.grid.elements[7][2].x, self.grid.elements[7][2].y)
        # print(self.grid.elements[7][1].x, self.grid.elements[7][1].y)
        # print(self.grid.elements[7][0].x, self.grid.elements[7][0].y)







