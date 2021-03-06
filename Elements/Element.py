from pprint import pprint


class Element:

    def __init__(self):
        self.H_matrix = []
        self.C_matrix = []
        self.P_vector = []
        self.nodes_array = []
        self.id_array = []

    def create_ids_array(self):
        id_array = []
        [id_array.append(node.id) for node in self.nodes_array]
        self.id_array = id_array

    def get_bc_array(self):
        return [self.nodes_array[0].bc, self.nodes_array[1].bc, self.nodes_array[2].bc, self.nodes_array[3].bc]


    def print_id_array(self):
        pprint(self.id_array[1].print_xy(), self.id_array[2].print_xy())
        pprint(self.id_array[0].print_xy(), self.id_array[3].print_xy())
        print("\n")
