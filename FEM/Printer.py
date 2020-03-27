from copy import copy

class Printer:


    def print_grid(self, grid, n_h):
        node = []
        for i in range(0, len(grid.nodes)):
            try:
                node.append([round(grid.nodes[i].x, 2), round(grid.nodes[i].y, 2)])
            except IndexError:
                continue
        matrix = [node[i:i + n_h] for i in range(0, len(node), n_h)]
        t_matrix = zip(*matrix)
        for row in t_matrix:
            print(row)



    def print_corner(self, grid):
        print(grid.elements[0][3].x, grid.elements[0][3].y)
        print(grid.elements[0][2].x, grid.elements[0][2].y)
        print(grid.elements[0][1].x, grid.elements[0][1].y)
        print(grid.elements[0][0].x, grid.elements[0][0].y)
        print("\n")
        print(grid.elements[3][3].x, grid.elements[3][3].y)
        print(grid.elements[3][2].x, grid.elements[3][2].y)
        print(grid.elements[3][1].x, grid.elements[3][1].y)
        print(grid.elements[3][0].x, grid.elements[3][0].y)

