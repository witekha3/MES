

class Calculator:

    def __init__(self, eta_array, ksi_array, x, y):
        self.eta_array = eta_array
        self.ksi_array = ksi_array
        self.x = x
        self.y = y
        self.dx_dEta = self.calculate_dXY(self.x, self.calculate_dNT_eta()[0])
        self.dx_dKsi = []
        self.dy_dEta = []
        self.dy_dKsi = []
        print(self.dx_dEta)


    def calculate_dNT_eta(self):
        dN1 = round((-0.25 * (1 - self.eta_array[0])).real, 5)
        dN2 = round((0.25 * (1 - self.eta_array[1])).real, 5)
        dN3 = round((0.25 * (1 + self.eta_array[2])).real, 5)
        dN4 = round((-0.25 * (1 + self.eta_array[3])).real, 5)
        return [dN1, dN2, dN3, dN4]

    def calculate_dNT_ksi(self):
        dN1 = round((-0.25 * (1 - self.eta_array[0])).real, 5)
        dN2 = round((-0.25 * (1 + self.eta_array[1])).real, 5)
        dN3 = round((0.25 * (1 + self.eta_array[2])).real, 5)
        dN4 = round((0.25 * (1 - self.eta_array[3])).real, 5)
        return [dN1, dN2, dN3, dN4]


    def calculate_dXY(self, tab, dNT):
        d=0
        for i in range(0,len(tab)):
            d += dNT[i] * tab[i]
        return d



    def calculate_det(row1, row2):
        return round((row1[0] * row2[1] - row1[1] * row2[1]).real, 8)