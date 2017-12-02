import random

import numpy as np

from lesson1 import Util


def getPerceptron(N):
    data = Util.dataGeneration(N)
    x = data[0]
    y = data[1]
    w = [0, 0, 0]
    count = 0
    while True:
        I = []
        for i in range(N):
            if np.sign(Util.getH(w, x[i])) != y[i]:
                I.append(i)

        count += 1
        if not I:
            break
        index = random.choice(I)
        w = Util.getW(w, y[index], x[index])
    return w, count


def getAverageNumberOfIteration(N):
    count = 0
    for i in range(1000):
        count += getPerceptron(N)[1]
    return count / 1000


def getFrequency(n):
    data = Util.dataGeneration(100000)

    x = data[0]
    y = data[1]

    w = getPerceptron(n)[0]
    frequency = 0
    for i in range(100000):
        if np.sign(Util.getH(w, x[i])) != y[i]:
            frequency += 1
    return frequency / 100000