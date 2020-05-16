import timeit

from MESSymulator import MESSymulator

if __name__ == "__main__":
    start = timeit.default_timer()
    simulator = MESSymulator()
    simulator.start()
    stop = timeit.default_timer()
    print('Time: ', stop - start)


