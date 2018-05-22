import numpy as np
import matplotlib.pyplot as plt


class Utilities:

    @staticmethod
    def norma_faster_gradient_descent(g):
        s = 0
        for i in range(0, len(g)):
            s = s + g[i] ** 2
        return np.sqrt(s)

    @staticmethod
    def norma_mcvard(x):
        return np.sqrt(x[0] ** 2 + x[1] ** 2)

    @staticmethod
    def plot_anim(x, xmax, xmin):
        plt.clf()
        for i in range(0, len(x)):
            axes = plt.gca()
            axes.set_xlim([xmin, xmax])
            axes.set_ylim([xmin, xmax])
            plt.plot(x[i][0], x[i][1], 'ro')
        plt.pause(0.1)

    # Виводимо результат методу
    @staticmethod
    def print_res(method_name="none", res=None):
        print()
        print("-" * 50)
        print(method_name)
        print()
        print("x:   ", res[0])
        print("f(x):", res[1])
        print("iter:", res[2])
        print("-" * 50)
