import numpy as np

from team5.lib5.Team5 import *


# Виводимо результат методу
def print_res(method_name="none", res=None):
    print()
    print("-" * 50)
    print(method_name)
    print()
    print("x:   ", res[0])
    print("f(x):", res[1])
    print("iter:", res[2])
    print("-" * 50)


# Тестовий приклад
def f1(x):
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


# Тестовий приклад
def f2(x):
    return 4. * (x[0] - 5) ** 2 + (x[1] - 6) ** 2



# Створюємо обєкт класа Team5
team5 = Team5()

# ----------------------------------------------------------
# Тест методу рою частинок
s = 40
d = 2

swarm_parties_name = "Метод рою частинок"
swarm_parties_res = team5.swarm_parties(s, d, f1)

print_res(swarm_parties_name, swarm_parties_res)

# ----------------------------------------------------------


# ----------------------------------------------------------
# Тест методу Макварада

x0 = np.array([8., 9.])
eps = 10 ** (-20)
u = 10 ** 2

mcvard_name = "Метод Макварада"
mcvard_res = team5.mcvard(x0, eps, u, f2)

print_res(mcvard_name, mcvard_res)

# ----------------------------------------------------------


# ----------------------------------------------------------
# Тест методу Хука-Джівса
x = np.array([1,3])

h = 0.5
a = 1
lam = 1

huca_jivsa_name: str = "Метод Хука-Дживса"
huca_jivsa_res = team5.huca_jivsa(x, h, a, lam, f2)

print_res(huca_jivsa_name, huca_jivsa_res)

# ----------------------------------------------------------
