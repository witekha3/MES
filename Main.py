import timeit
from cmath import sqrt
from pprint import pprint

from Creator import Creator
from Elements.Grid import Grid

if __name__ == "__main__":
    start = timeit.default_timer()

    Creator().create_nodes_for_grid()
    Creator().create_elements_for_grid()
#    print(Grid().global_matrix_C)
    stop = timeit.default_timer()

    print('Time: ', stop - start)


