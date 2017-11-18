import random


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