from random import *

from numpy import linalg

from team5.utilities.Utilities import *


class Team5:
    # --------------------------------------------------------------------------------
    """Метод золотого перерізу"""

    @staticmethod
    def golden_section(a, b, f, eps=10 ** (-4), t=0.38196):

        k = 0
        while abs(a - b) > eps:
            y = a + t * (b - a)
            z = a + b - y
            fy = f(y)
            fz = f(z)

            if fy <= fz:
                b = z
            else:
                a = y

            k += 1

        x_min = (a + b) / 2

        return x_min, f(x_min), k

    # --------------------------------------------------------------------------------
    """ Метод хорд """

    @staticmethod
    def toxins(a, b, f, df, eps=10 ** (-4)):

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

    # ----------------------------------------------------------------------------------
    """ Метод Хука-Дживса """

    @staticmethod
    def huca_jivsa(x0, f, delta=0.5, alpha=2., lamb=1., eps=10e-4):
        n = len(x0)

        x1 = np.zeros(n, dtype=np.float)
        k = 1

        while delta > eps and k < 450:
            y1 = np.zeros(n, dtype=np.float)

            for i in range(0, n):

                y0 = x0.copy()
                y0[i] = y0[i] + delta

                if f(y0) < f(x0):
                    y1[i] = y0[i]
                else:
                    y0[i] = y0[i] - 2 * delta
                    if f(y0) < f(x0):
                        y1[i] = y0[i]
                    else:
                        y1[i] = x0[i]

            if f(y1) < f(x0):
                x1 = y1.copy()
                x1 = x1 + lamb * (x1 - x0)
                x0 = x1.copy()
            else:
                delta = delta / alpha

            k = k + 1

        return [x1, f(x1), k]

    # -------------------------------------------------------------------------------
    """ Метод дихотомії"""

    @staticmethod
    def dichotomy(x0, f, gradient, a=-5, b=6, eps=10 ** (-6)):

        delta = eps / 10

        while abs(b - a) > eps:
            alpha1 = (a + b - delta) / 2
            alpha2 = (a + b + delta) / 2

            f1 = f(x0 - alpha1 * gradient(x0))
            f2 = f(x0 - alpha2 * gradient(x0))

            if f1 < f2:
                b = alpha2
            else:
                a = alpha1

        return (a + b) / 2

    # --------------------------------------------------------------------------------
    """ Найшвідшого градієнтного спуску """
    @staticmethod
    def faster_gradient_descent(x0, f, gradient, eps=10 ** (-4)):
        k = 1

        p = -gradient(x0)

        alpha = Team5.dichotomy(x0, f, gradient)

        x1 = x0 + alpha * p

        while Utilities.norma_faster_gradient_descent(gradient(x1)) > eps:
            b = Utilities.norma_faster_gradient_descent(gradient(x1)) ** 2 / Utilities.norma_faster_gradient_descent(
                gradient(x0)) ** 2
            p = - gradient(x1) + b * p

            x0 = x1
            alpha = Team5.dichotomy(x0, f, gradient)

            x1 = x0 + alpha * p

            k += 1

        return [x1, f(x1), k]

    # --------------------------------------------------------------------------------
    """ Метод Макварда """

    @staticmethod
    def mcvard(x0, f, gradient, hesse, eps=10 ** (-20), u=10 ** 2, max_iter=50):
        k = 0

        x1 = np.array([])

        E = np.array([[1, 0], [0, 1]])

        while Utilities.norma_mcvard(gradient(x0)) >= eps and k < max_iter:
            x1 = x0 - np.dot(linalg.inv(hesse(x0) + u * E), gradient(x0))

            if f(x1) < f(x0):
                u /= 2
            else:
                u *= 2

            x0 = x1.copy()
            k += 1

        return x1, f(x1), k

    # --------------------------------------------------------------------------------
    """ Метод рою частиць """

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
                Utilities.plot_anim(x, xmax, xmin)

        return fp[gbest], p[gbest], k
