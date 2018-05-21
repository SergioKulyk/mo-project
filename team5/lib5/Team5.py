from random import *

import numpy as np

import matplotlib.pyplot as plt

from numpy import linalg


class Team5:
    """"""

    def __init__(self):
        """Constructors"""
        pass

    # --------------------------------------------------------------------------------

    '''Метод хорд'''
    @staticmethod
    def toxins(a, b, f, df, eps=10**(-4)):

        k = 0
        x = a - (a + b) * df(a) / (df(a) - df(b))

        while abs(df(x)) > eps:
            if df(x) > 0:
                b = x
            else:
                a = x

            k += 1
            x = a - (a + b) * df(a) / (df(a) - df(b))

        return x, f(x), k

    # --------------------------------------------------------------------------------

    # Метод рою частиць
    @staticmethod
    def swarm_parties(s, d, f, swarm=50, xmin=-10, xmax=10, w=0.72, c1=1.19, c2=1.19, plot_animation=False):
        k = 1

        x = np.zeros((s, d))
        v = np.zeros((s, d))
        p = np.zeros((s, d))
        fitness = np.zeros(s)

        fp = np.zeros(s)

        if plot_animation:
            plt.show()

        for i in range(0, s):
            for j in range(0, d):
                x[i][j] = uniform(xmin, xmax)
                v[i][j] = (uniform(xmin, xmax) - x[i][j]) / 2
                p[i][j] = x[i][j]

            fitness[i] = f(x[i])
            fp[i] = fitness[i]

        gbest = 0
        for i in range(1, s):
            if fp[i] < fp[gbest]:
                gbest = i

        while k <= swarm:
            for i in range(0, s):
                for j in range(0, d):
                    r1 = uniform(0, 1)
                    r2 = uniform(0, 1)

                    v[i][j] = w * v[i][j] + c1 * r1 * (p[i][j] - x[i][j])

                    if i != gbest:
                        v[i][j] = v[i][j] + c2 * r2 * (p[gbest][j] - x[i][j])

                    x[i][j] = x[i][j] + v[i][j]

                    if x[i][j] < xmin:
                        x[i][j] = xmin
                        v[i][j] = 0
                    if x[i][j] > xmax:
                        x[i][j] = xmax
                        v[i][j] = 0

            for i in range(0, s):
                fitness[i] = f(x[i])
                if fitness[i] < fp[i]:
                    fp[i] = fitness[i]
                    for j in range(0, d):
                        p[i][j] = x[i][j]

            for i in range(0, s):
                if fp[i] < fp[gbest]:
                    gbest = i
            k += 1

            if plot_animation:
                Team5.plot_anim(x, xmax, xmin)

        return fp[gbest], p[gbest], k

    @staticmethod
    def plot_anim(x, xmax, xmin):
        plt.clf()
        for i in range(0, len(x)):
            axes = plt.gca()
            axes.set_xlim([xmin, xmax])
            axes.set_ylim([xmin, xmax])
            plt.plot(x[i][0], x[i][1], 'ro')
        plt.pause(0.1)

    # --------------------------------------------------------------------------------

    # Метод Макварда

    # Допоміжний метод
    @staticmethod
    def gradient(x):
        return np.array([8. * (x[0] - 5), 2 * (x[1] - 6)])

    # Допоміжний метод
    @staticmethod
    def hesse(x0):
        return np.array([[8., 0], [0, 2.]])

    # Норма x.
    @staticmethod
    def norma(x):
        return np.sqrt(x[0] ** 2 + x[1] ** 2)

    @staticmethod
    def mcvard(x0, eps, u, f, max_iter=50):
        k = 0

        x1 = np.array([])

        E = np.array([[1, 0], [0, 1]])

        while Team5.norma(Team5.gradient(x0)) >= eps and k < max_iter:
            x1 = x0 - np.dot(linalg.inv(Team5.hesse(x0) + u * E), Team5.gradient(x0))

            if f(x1) < f(x0):
                u /= 2
            else:
                u *= 2

            x0 = x1.copy()
            k += 1

        return x1, f(x1), k

    # --------------------------------------------------------------------------------

    # Метод Хука-Дживса
    @staticmethod
    def huca_jivsa(x, h, a, lam, f, eps=10e-4):
        k = 0

        y = x
        y1 = x

        while Team5.norma_huca_jivsa(x) <= eps:
            if f([y[0] + h, y[1]]) < f(y):
                if f([y[0] + h, y[1] + h]) < f(y):
                    y1 = y1 + h
                elif f([y[0] + h, y[1] - h]) < f(y):
                    y1[0] = y1[0] + h
                    y1[1] = y1[1] - h
            elif f([y[0] - h, y[1]]) < f(y):
                if f([y[0] - h, y[1] + h]) < f(y):
                    y1[0] = y1[0] - h
                    y1[1] = y1[1] + h
                elif f([y[0] - h, y[1] - h]) < f(y):
                    y1 = y1 - h
            else:
                y1 = y

            if f(y1) < f(y):
                x1 = y1
                y = x1 + lam * (x1 - x)
            else:
                pass

            h /= a
            y = x
            k += 1
            print(x)

        return x, f(x), k

    def norma_huca_jivsa(x):
        return max(map(abs, x))



