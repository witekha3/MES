class IntegralCalculator:

    @staticmethod
    def calculate_1D_2points_integral(N, points_array, w):
        integral = 0
        for i in range(0, N):
            integral += w[i] * (5 * points_array[i] * points_array[i] + 3 * points_array[i] + 6)
        print(integral)

    @staticmethod
    def calculate_1D_3points_integral(N, points_array, w):
        integral = 0
        for i in range(0, N):
            integral += w[i] * (5 * points_array[i] * points_array[i] + 3 * points_array[i] + 6)
        print(integral)

    @staticmethod
    def calculate_2D_2points_integral(N, points_array, w):
        integral = 0
        for i in range(0, N):
            for j in range(0, N):
                integral += w[i] * (5 * pow(points_array[i], 2) * pow(points_array[j], 2)
                                    + 3 * points_array[i] * points_array[j] + 6)
        print(integral)

    @staticmethod
    def calculate_2D_3points_integral(N, points_array, w):
        integral = 0
        for i in range(0, N):
            for j in range(0, N):
                integral += w[i] * w[j] * (5 * pow(points_array[i], 2) * pow(points_array[j], 2)
                                           + 3 * points_array[i] * points_array[j] + 6)
        print(integral)
