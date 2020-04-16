from GlobalData import GlobalData


class Grid:
    nodes = []
    elements = []

    @staticmethod
    def print_nodes():
        for node in Grid.nodes:
            node.print_xy()

    @staticmethod
    def print_elements():
        for element in Grid.elements:
            element.print_id_array()

