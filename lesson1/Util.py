import random


def pointGeneration():
    return [random.uniform(-1, 1), random.uniform(-1, 1)]


point1 = pointGeneration()
point2 = pointGeneration()


def dataGeneration(N):
    x = [[1, random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(N)]
    y = []
    for i in range(N):
        if func(x[i][1]) > x[i][2]:
            y.append(-1)
        else:
            y.append(1)
    return x, y


def func(x):
    return (((x - point1[0]) * (point2[1] - point1[0])) / (point2[0] - point1[0])) + point1[1]


def position(y, x):
    if y > x:
        Y = -1
    else:
        Y = 1
    return Y


def getH(w, x):
    y = 0
    for i in range(3):
        y += w[i] * x[i]
    return y


def getW(w, y, x):
    newW = w
    for i in range(3):
        newW[i] += y * x[i]
    return newW