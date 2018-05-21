from random import *

from numpy import *

import matplotlib.pyplot as plt


class Team5:
    """"""

    def __init__(self):
        """Constructors"""
        pass

    @staticmethod
    def swarm_parties(s, d, f, swarm=50, xmin=-10, xmax=10, w=0.72, c1=1.19, c2=1.19, plot_animation=False):
        k = 1

        x = zeros((s, d))
        v = zeros((s, d))
        p = zeros((s, d))
        fitness = zeros(s)

        fp = zeros(s)

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

