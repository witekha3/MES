from cmath import sqrt


class UniversalElement:

    def __init__(self):
        self.ksi = [-1/sqrt(3), 1/sqrt(3), 1/sqrt(3), -1/sqrt(3)]
        self.eta = [-1/sqrt(3), -1/sqrt(3), 1/sqrt(3), 1/sqrt(3)]
        self.xT = [0, 0.025, 0.025, 0]
        self.yT = [0, 0, 0.025, 0.025]

        Calculator(self.eta, self.ksi, self.xT, self.yT)

UniversalElement()