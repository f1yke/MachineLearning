import math
import random

import numpy as np

from lesson1 import Util as Util1
from lesson2 import Util as Util2


def getDistribution(countIter):
    v = Util1.dataGeneration(countIter)
    result = []
    for i in range(3):
        fIter = []
        vIter = sorted(set(v[i]))
        pIter = [v[i].count(j) / countIter for j in vIter]
        fIter.append(0)
        print(vIter)
        for k in range(len(vIter) - 1):
            fIter.append(fIter[k] + pIter[k])
        hIter = [1 - 2 * math.pow(math.e, -2 * countIter * math.pow(l, 2)) for l in vIter]
        flag = True
        for l in range(len(fIter)):
            if fIter[l] < hIter[l]:
                flag = False
                break
        result.append(flag)
    return result


def getFreq(countIter):
    count = 0
    for i in range(countIter):
        data = Util1.dataGeneration(100)
        x = np.array(data[0])
        y = np.array(data[1])
        w = np.dot(np.dot(np.linalg.matrix_power(np.dot(x.T, x), -1), x.T), y)
        h = [np.sign(np.dot(w, t.T)) for t in x]
        for j in range(countIter):
            if y[i] != h[i]:
                count += 1
    return count / 100 * countIter


def getFreq(countPoints, countIter):
    l = Util2.lineGeneration()
    x = np.array(np.array([[1, random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(100)]))
    y = np.array([Util1.position(Util2.f(t[1], l), t[2]) for t in x])
    w = np.dot(np.dot(np.linalg.matrix_power(np.dot(x.T, x), -1), x.T), y)
    count = 0
    for i in range(countIter):
        x = np.array(np.array([[1, random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(countPoints)]))
        y = np.array([Util1.position(Util2.f(t[1], l), t[2]) for t in x])
        h = [np.sign(np.dot(w, t.T)) for t in x]
        for j in range(countPoints):
            if y[i] != h[i]:
                count += 1
    return count / (countPoints * countIter)


def pla(countIter):
    count = 0
    for i in range(countIter):
        l = Util2.lineGeneration()
        x = np.array(np.array([[1, random.uniform(-1, 1), random.uniform(-1, 1)] for i in range(10)]))
        y = np.array([Util1.position(Util2.f(t[1], l), t[2]) for t in x])
        w = np.dot(np.dot(np.linalg.matrix_power(np.dot(x.T, x), -1), x.T), y)
        while True:
            I = []
            for i in range(10):
                if np.sign(Util1.getH(w, x[i])) != y[i]:
                    I.append(i)
            if not I:
                break
            index = random.choice(I)
            w = Util1.getW(w, y[index], x[index])
            count += 1
    return count / countIter


def task5(countIter, countPoints):
    count = 0
    for i in range(countIter):
        x, y = Util2.dataGenWithNoise(countPoints)
        w = np.dot(np.dot(np.linalg.matrix_power(np.dot(x.T, x), -1), x.T), y)
        h = [np.sign(np.dot(w, t.T)) for t in x]
        for i in range(countPoints):
            if y[i] != h[i]:
                count += 1
    return count / (countIter * countPoints)


def task6(countIter, countPoints):
    aFreq = 0
    bFreq = 0
    cFreq = 0
    dFreq = 0
    eFreq = 0
    for i in range(countIter):
        x, y = dataGenWithNoise(countPoints)
        x = np.array(x)
        y = np.array(y)
        w = np.dot(np.dot(np.linalg.matrix_power(np.dot(x.T, x), -1), x.T), y)
        t = x[random.randint(0, countPoints - 1)]
        h = np.sign(np.dot(w, t.T))
        if Util2.ga(t) != h:
            aFreq += 1
        if Util2.gb(t) != h:
            bFreq += 1
        if Util2.gc(t) != h:
            cFreq += 1
        if Util2.gd(t) != h:
            dFreq += 1
        if Util2.ge(t) != h:
            eFreq += 1
    return aFreq / countIter, bFreq / countIter, cFreq / countIter, dFreq / countIter, eFreq / countIter


def dataGenWithNoise(countPoints):
    noise = Util2.noiseGen(countPoints)
    x = Util2.genX(countPoints)
    y = []
    for i in range(countPoints):
        t = Util2.f(x[i])
        if (noise[i] == -1):
            t = -t
        y.append(t)
    return x, y


def task7(countIter, countPoints):
    x, y = dataGenWithNoise(countPoints)
    x = np.array(x)
    y = np.array(y)
    w = np.dot(np.dot(np.linalg.matrix_power(np.dot(x.T, x), -1), x.T), y)
    count = 0
    for i in range(countIter):
        x, y = dataGenWithNoise(countPoints)
        x = np.array(x)
        y = np.array(y)
        h = [np.sign(np.dot(w, t.T)) for t in x]
        for i in range(countPoints):
            if y[i] != h[i]:
                count += 1
    return count / (countIter * countPoints)