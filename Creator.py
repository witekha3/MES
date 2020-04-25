from copy import copy

from Elements.Element import Element
from Elements.Grid import Grid
from Elements.Node import Node
from Elements.UniversalElement import UniversalElement
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
        node_id = 0
        for i in range(0, self.n_H):
            node = Node()
            for j in range(0, self.n_W):
                node.x = i * self.lx
                node.y = j * self.ly
                node.id = node_id
                Grid.nodes.append(copy(node))
                node_id += 1


    def create_elements_for_grid(self):
        height_counter = 0
        for i in range(0, len(Grid.nodes)):
            try:
                element = Element()
                height_counter += 1
                if height_counter == (self.n_H -1):
                    height_counter = 0
                    continue
                element.id_array.append(Grid.nodes[i].id)
                element.id_array.append(Grid.nodes[i+4].id)
                element.id_array.append(Grid.nodes[i+5].id)
                element.id_array.append(Grid.nodes[i+1].id)
                x_array = [Grid.nodes[i].x, Grid.nodes[i+4].x, Grid.nodes[i+5].x, Grid.nodes[i+1].x]
                y_array = [Grid.nodes[i].y, Grid.nodes[i+4].y, Grid.nodes[i+5].y, Grid.nodes[i+1].y]
                universal_element = UniversalElement(x_array, y_array)
                element.H_matrix = universal_element.H_matrices
                element.C_matrix = universal_element.C_matrices
                Grid.elements.append(element)
            except IndexError:
                continue
