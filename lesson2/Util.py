import math
import random

import numpy as np


def dataGeneration(iter):
    v1 = []
    v_min = []
    v_rand = []
    for i in range(iter):
        c = []
        min = 0
        for j in range(1000):
            count = 0
            for k in range(10):
                tmp = random.randint(0, 1)
                if tmp == 1:
                    count += 1
            freq = count / 10
            if freq < min:
                min = freq
            c.append(freq)
        v1.append(c[0])
        v_min.append(min)
        v_rand.append(random.choice(c))
    return v1, v_min, v_rand


def lineGeneration():
    return [[random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(2)]


def f(x, l):
    return (((x - l[0][0]) * (l[1][1] - l[0][1])) / (l[1][0] - l[0][0])) + l[0][1]


def f(x):
    return np.sign(math.pow(x[1], 2) + math.pow(x[2], 2) - 0.6)


def noiseGen(countPoints):
    count = 0
    noise = np.ones(countPoints)
    while True:
        index = random.randint(0, countPoints - 1)
        if (noise[index] == 1):
            noise[index] = -1
            count += 1
        if (count == countPoints / 10):
            break
    return noise


def dataGenWithNoise(countPoints):
    noise = noiseGen(countPoints)
    x = np.array([[1, random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(countPoints)])
    y = []
    for i in range(countPoints):
        t = f(x[i])
        if (noise[i] == -1):
            t = -t
        y.append(t)
    return x, y


def ga(x):
    return np.sign(
        -1 - 0.05 * x[1] + 0.08 * x[2] + 0.13 * x[1] * x[2] + 1.5 * math.pow(x[1], 2) + 1.5 * math.pow(x[2], 2))


def gb(x):
    return np.sign(
        -1 - 0.05 * x[1] + 0.08 * x[2] + 0.13 * x[1] * x[2] + 1.5 * math.pow(x[1], 2) + 15 * math.pow(x[2], 2))


def gc(x):
    return np.sign(
        -1 - 0.05 * x[1] + 0.08 * x[2] + 0.13 * x[1] * x[2] + 15 * math.pow(x[1], 2) + 1.5 * math.pow(x[2], 2))


def gd(x):
    return np.sign(
        -1 - 1.05 * x[1] + 0.08 * x[2] + 0.13 * x[1] * x[2] + 0.05 * math.pow(x[1], 2) + 0.05 * math.pow(x[2], 2))


def ge(x):
    return np.sign(
        -1 - 0.05 * x[1] + 0.08 * x[2] + 1.5 * x[1] * x[2] + 0.15 * math.pow(x[1], 2) + 0.15 * math.pow(x[2], 2))


def genX(N):
    x = []
    for _ in range(N):
        temp = [random.uniform(-1, 1), random.uniform(-1, 1)]
        x.append([1, temp[0], temp[1], temp[0] * temp[1], math.pow(temp[0], 2), math.pow(temp[1], 2)])
    return x
