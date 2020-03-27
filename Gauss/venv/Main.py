from cmath import sqrt
from functools import reduce
# def calucalte(N, p1, w):
#     integral = 0
#     for i in range(0, N):
#         integral += w[i] * (5*p1[i]*p1[i] + 3*p1[i] + 6)
#     print(integral)
#
#
#
# if __name__ == "__main__":
#     p1 = [-1/sqrt(3), 1/sqrt(3)]
#     p2 = [-sqrt(3/5), sqrt(3/5)]
#
#     calucalte(2, p1, [1,1]);


###########################################################################3

# def calucalte2(N, p1, w):
#     integral = 0
#     for i in range(0, N):
#         integral += w[i] * (5*p1[i]*p1[i] + 3*p1[i] + 6)
#     print(integral)
#
#
#
# if __name__ == "__main__":
#     p2 = [-sqrt(3/5), 0, sqrt(3/5)]
#     w2 = [5/9, 8/9, 5/9]
#
#     calucalte2(3, p2, w2);

#############################################################################
#
# def calucalte2(N, p1, w):
#     integral = 0
#     for i in range(0, N):
#         for j in range(0, N):
#             integral += w[i] * w[j] * (5 * pow(p1[i], 2) * pow(p1[j],2) + 3 * p1[i] * p1[j] + 6)
#     print(integral)
#
#
#
# if __name__ == "__main__":
#     p1 = [-1/sqrt(3), 1/sqrt(3)]
#     p2 = [-sqrt(3/5), sqrt(3/5)]
#
#     calucalte2(2, p1, [1,1]);


########################################################################
def calucalte2(N, p1, w):
    integral = 0
    for i in range(0, N):
        for j in range(0, N):
            integral += w[i] * w[j] * (5 * pow(p1[i], 2) * pow(p1[j],2) + 3 * p1[i] * p1[j] + 6)
    print(integral)
#
#
#
if __name__ == "__main__":
    p2 = [-sqrt(3/5), 0, sqrt(3/5)]
    w2 = [5/9, 8/9, 5/9]

    calucalte2(3, p2, w2);
