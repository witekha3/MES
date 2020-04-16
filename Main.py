from cmath import sqrt

from Creator import Creator
from Elements.Grid import Grid
from Elements.UniversalElement import UniversalElement

if __name__ == "__main__":
    Creator().create_nodes_for_grid()
    Creator().create_elements_for_grid()
    # x_array = []
    # y_array = []
    # ksi_array = [-1/sqrt(3), 1/sqrt(3), 1/sqrt(3), -1/sqrt(3)]
    # eta_array = [-1/sqrt(3), -1/sqrt(3), 1/sqrt(3), 1/sqrt(3)]
    # for element in Grid.elements:
    #
    #     for node in element.id_array:
    #         x_array.append(node.x)
    #         y_array.append(node.y)
    #     universal_element = UniversalElement(ksi_array, eta_array, x_array, y_array)
    #     print(universal_element.H_matrices)
    #     print("\n")
    #     print(universal_element.C_matrices)
    #
    #     break


