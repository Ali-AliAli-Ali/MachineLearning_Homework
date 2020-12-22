import random
import math
from math import exp, log
import numpy as np
from numpy import linalg, arange
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(8, 8))
maxX = 0
n = 100#random.randint(10, 1000)
mode = input("Set the mode: lin, pol or exp - ")


if mode == 'lin':
    A = np.ones((n, 2))
    AT = np.ones((2, n))
    Y = np.ones((n, 1))
    for i in range(0, n):
        x = i
        maxX = max(maxX, x)
        y = random.randint(0, i*20)#20*i + random.randint(1, 33)# random.randint(0, i)
        plt.scatter(x, y)
        A[i][1] = AT[1][i] = x
        Y[i][0] = y

    omega = np.dot(np.dot(linalg.inv(np.dot(AT, A)), AT), Y)

    Xes = arange(0, maxX, 0.01)
    plt.plot(Xes, omega[0][0] + omega[1][0] * Xes)


elif mode == 'pol':
    degree = int(input("Enter the degree then - "))
    degree += 1

    A = np.ones((n, degree))
    AT = np.ones((degree, n))
    Y = np.ones((n, 1))
    for i in range(0, n):
        x = i
        maxX = max(maxX, x)
        y = random.randint(0, i*20)#i+i*i+i*i*i+i*i*i*i + random.randint(0, 5)
        plt.scatter(x, y)

        for j in range(1, degree):
            A[i][j] = AT[j][i] = pow(x, j)
        Y[i][0] = y

    omega = np.dot(np.dot(linalg.inv(np.dot(AT, A)), AT), Y)

    Xes = arange(0, maxX, 0.01)
    sum = 0
    for i in range(degree): sum += omega[i][0] * pow(Xes, i)
    plt.plot(Xes, sum)


else:
    A = np.ones((n, 2))
    AT = np.ones((2, n))
    Y = np.ones((n, 1))
    for i in range(0, n):
        x = i
        maxX = max(maxX, x)
        y = random.randint(1, (i+1)*20)#exp(i)
        plt.scatter(x, y)
        A[i][1] = AT[1][i] = x
        Y[i][0] = log(y)

    omega = np.dot(np.dot(linalg.inv(np.dot(AT, A)), AT), Y)
    print(omega)
    Xes = arange(0, maxX, 0.01)

    plt.plot(Xes, pow(math.e, omega[0][0] + omega[1][0] * Xes))

plt.show()
