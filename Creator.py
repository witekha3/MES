from copy import copy

from Elements.Element import Element
from Elements.Grid import Grid
from Elements.Node import Node
from GlobalData import GlobalData


class Creator:

    def __init__(self):
        self.H = GlobalData().H
        self.W = GlobalData().W
        self.n_H = GlobalData().n_H
        self.n_W = GlobalData().n_W
        self.lx = self.W / (self.n_W - 1)
        self.ly = self.H / (self.n_H - 1)


    def create_nodes_for_grid(self):
        for i in range(0, self.n_H):
            node = Node()
            for j in range(0, self.n_W):
                node.x = i * self.lx
                node.y = j * self.ly
                Grid.nodes.append(copy(node))


    def create_elements_for_grid(self):
        height_counter = 0
        for i in range(0, len(Grid.nodes)):
            try:
                element = Element()
                height_counter += 1
                if height_counter == (self.n_H -1):
                    height_counter = 0
                    continue
                element.id_array.append(copy(Grid.nodes[i]))
                element.id_array.append(copy(Grid.nodes[i+4]))
                element.id_array.append(copy(Grid.nodes[i+5]))
                element.id_array.append(copy(Grid.nodes[i+1]))
                Grid.elements.append(element)
            except IndexError:
                continue
