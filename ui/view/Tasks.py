from _datetime import datetime

from lesson2 import Service


def task1(countIter):
    start = datetime.now()
    print(Service.getDistribution(countIter))
    end = datetime.now()
    print(end - start)


def task2(countIter):
    start = datetime.now()
    print(Service.getFreq(countIter))
    end = datetime.now()
    print(end - start)


def task3(countPoint, countIter):
    start = datetime.now()
    print(Service.getFreq(countPoint, countIter))
    end = datetime.now()
    print(end - start)


def task4(countIter):
    start = datetime.now()
    print(Service.pla(countIter))
    end = datetime.now()
    print(end - start)


def task5(countIter, countPoints):
    start = datetime.now()
    print(Service.task5(countIter, countPoints))
    end = datetime.now()
    print(end - start)


def task6(countIter, countPoints):
    start = datetime.now()
    print(Service.task6(countIter, countPoints))
    end = datetime.now()
    print(end - start)


def task7(countIter, countPoints):
    start = datetime.now()
    print(Service.task7(countIter, countPoints))
    end = datetime.now()
    print(end - start)