from copy import copy, deepcopy

from Elements.Element import Element
from Elements.Grid import Grid
from Elements.Node import Node
from Elements.UniversalElement import UniversalElement
from GlobalData import GlobalData


class Creator:

    def __init__(self):
        global_data = GlobalData()
        self.H = global_data.H
        self.W = global_data.W
        self.n_H = global_data.n_H
        self.n_W = global_data.n_W
        self.lx = self.W / (self.n_W - 1)
        self.ly = self.H / (self.n_H - 1)

    def set_bc(self, node):
        if node.x == 0 or node.y == 0 or node.x == self.W or node.y == self.H:
            node.bc = True
        else:
            node.bc = False

    def create_nodes_for_grid(self):
        node_id = 0
        for i in range(0, self.n_H):
            node = Node()
            for j in range(0, self.n_W):
                node.x = i * self.lx
                node.y = j * self.ly
                node.id = node_id
                self.set_bc(node)
                Grid.nodes.append(copy(node))
                node_id += 1

    def create_elements_for_grid(self):
        height_counter = 0
        for i in range(0, len(Grid.nodes)):
            try:
                element = Element()
                height_counter += 1
                if height_counter > (self.n_H - 1):
                    height_counter = 0
                    continue
                self.add_nodes_to_element(element, i)
                self.create_H_C_P_for_element(element, i)
                Grid.elements.append(element)
            except IndexError:
                continue

    def add_nodes_to_element(self, element, node_id):
        element.nodes_array.append(Grid.nodes[node_id])
        element.nodes_array.append(Grid.nodes[node_id + self.n_H])
        element.nodes_array.append(Grid.nodes[node_id + self.n_H + 1])
        element.nodes_array.append(Grid.nodes[node_id + 1])
        element.create_ids_array()

    def create_H_C_P_for_element(self, element, node_id):
        x_array = [Grid.nodes[node_id].x, Grid.nodes[node_id + self.n_H].x,
                   Grid.nodes[node_id + self.n_H + 1].x, Grid.nodes[node_id + 1].x]
        y_array = [Grid.nodes[node_id].y, Grid.nodes[node_id + self.n_H].y,
                   Grid.nodes[node_id + self.n_H + 1].y, Grid.nodes[node_id + 1].y]
        universal_element = UniversalElement(x_array, y_array, element.get_bc_array())
        element.H_matrix = universal_element.H_matrix
        element.C_matrix = universal_element.C_matrix
        element.P_vector = universal_element.P_vector
