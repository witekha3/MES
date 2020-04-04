from cmath import sqrt

from UniversalElementCalculator import UniversalElementCalculator


class UniversalElement:

    def __init__(self):
        self.ksi = [-1/sqrt(3), 1/sqrt(3), 1/sqrt(3), -1/sqrt(3)]
        self.eta = [-1/sqrt(3), -1/sqrt(3), 1/sqrt(3), 1/sqrt(3)]
        self.xT = [0, 0.025, 0.025, 0]
        self.yT = [0, 0, 0.025, 0.025]

        universal_element_calculator = UniversalElementCalculator(self.eta, self.ksi, self.xT, self.yT)
        print(universal_element_calculator.calculate_universal_element())

if __name__ == "__main__":
    UniversalElement()