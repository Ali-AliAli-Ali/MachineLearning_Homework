import numpy as np
import random

def amountTestDeterminer(amountPoints):
    if amountPoints <= 1000: return 100
    elif amountPoints <= 10000: return amountPoints // 100
    elif amountPoints <= 1000000: return amountPoints // 1000
    else: return amountPoints // 100000


def usual(amountPoints):
    amountTestPoints = amountTestDeterminer(amountPoints)

    Points = np.random.randint(0, 1000, (amountPoints, 3))
    testPoints = np.random.randint(0, 1000, (amountTestPoints, 2))

    return Points, testPoints


def line(amountPoints):
    amountTestPoints = amountTestDeterminer(amountPoints)
    Points = np.zeros((amountPoints, 3))
    testPoints = np.zeros((amountTestPoints, 2))

    for i in range(amountPoints):
        Points[i][0] = i
        Points[i][1] = i*20 + random.randint(-10000, 10000)
    for i in range(amountTestPoints):
        testPoints[i][0] = random.randint(0, amountPoints)
        testPoints[i][1] = testPoints[i][0]*20 + random.randint(-10000, 10000)

    return Points, testPoints

def lines3(amountPoints):
    amountTestPoints = amountTestDeterminer(amountPoints)
    Points = np.zeros((amountPoints, 3))
    testPoints = np.zeros((amountTestPoints, 2))

    for i in range(amountPoints//3):
        Points[i][0] = i
        Points[i][1] = i*20 + random.randint(-10000, 10000)
    for i in range(amountPoints//3, amountPoints//3*2):
        Points[i][0] = i
        Points[i][1] = i*20 + random.randint(-10000, 10000) + 50000
    for i in range(amountPoints//3*2, amountPoints):
        Points[i][0] = i
        Points[i][1] = i*20 + random.randint(-10000, 10000) + 100000

    for i in range(amountTestPoints):
        testPoints[i][0] = random.randint(0, amountPoints//3)
        testPoints[i][1] = testPoints[i][0]*20 + random.randint(-10000, 10000)
    for i in range(amountTestPoints):
        testPoints[i][0] = random.randint(amountPoints//3, amountPoints//3*2)
        testPoints[i][1] = testPoints[i][0]*20 + random.randint(-10000, 10000) + 50000
    for i in range(amountTestPoints):
        testPoints[i][0] = random.randint(amountPoints//3*2, amountPoints)
        testPoints[i][1] = testPoints[i][0]*20 + random.randint(-10000, 10000) + 100000

    return Points, testPoints


def circles(amountPoints):
    amountTestPoints = amountTestDeterminer(amountPoints)

    Points = np.zeros((amountPoints, 3))
    testPoints = np.zeros((amountTestPoints, 2))

    for i in range(amountPoints//4):
        Points[i][0] = i%2000
        Points[i][1] = np.math.sqrt(1000000 - (i % 2000 - 1000) * (i % 2000 - 1000)) + 1000
    for i in range(amountPoints//4, amountPoints//2):
        Points[i][0] = i%2000
        Points[i][1] = - np.math.sqrt(1000000 - (i % 2000 - 1000) * (i % 2000 - 1000)) + 1000
    for i in range(amountPoints//2, amountPoints//4*3):
        Points[i][0] = i%2000
        Points[i][1] = np.math.sqrt(13000000 - (i%2000 - 1000) * (i%2000 - 1000)) + 1000
    for i in range(amountPoints//4*3, amountPoints):
        Points[i][0] = i%2000
        Points[i][1] = - np.math.sqrt(13000000 - (i % 2000 - 1000) * (i % 2000 - 1000)) + 1000


    for i in range(amountTestPoints//4):
        testPoints[i][0] = random.randint(0, amountPoints//4)%2000
        testPoints[i][1] = np.math.sqrt(1000000 - (testPoints[i][0] % 2000 - 1000) * (testPoints[i][0] % 2000 - 1000)) + 1000
    for i in range(amountTestPoints//4, amountTestPoints//2):
        testPoints[i][0] = random.randint(0, amountPoints//4)%2000
        testPoints[i][1] = - np.math.sqrt(1000000 - (testPoints[i][0] % 2000 - 1000) * (testPoints[i][0] % 2000 - 1000)) + 1000
    for i in range(amountTestPoints//2, amountTestPoints//4*3):
        testPoints[i][0] = random.randint(0, amountPoints//4)%2000
        testPoints[i][1] = np.math.sqrt(13000000 - (testPoints[i][0] % 2000 - 1000) * (testPoints[i][0] % 2000 - 1000)) + 1000
    for i in range(amountTestPoints//4*3, amountTestPoints):
        testPoints[i][0] = random.randint(0, amountPoints//4)%2000
        testPoints[i][1] = - np.math.sqrt(13000000 - (testPoints[i][0] % 2000 - 1000) * (testPoints[i][0] % 2000 - 1000)) + 1000
    return Points, testPoints