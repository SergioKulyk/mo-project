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


f_golden_test = lambda x: x ** 3 - 27 * x + 5
f_huca_jivsa_test = lambda x: 4. * (x[0] - 5) ** 2 + (x[1] - 6) ** 2


def f1(x):
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


# Тестовий приклад


def f_toxins_test(x):
    return x ** 2 + x + np.sin(x)


def df_toxins_test(x):
    return 2 * x + 1 + np.cos(x)


def f_golden_test(x):
    return x ** 3 - 27 * x + 5


# Створюємо обєкт класа Team5
team5 = Team5()

# ----------------------------------------------------------
# Тест методу золотого перерізу
a = -4
b = 4

golden_section_name = "Метод золотого перерізу"
golden_section_res = Team5.golden_section(a, b, f_golden_test)

print_res(golden_section_name, golden_section_res)
# ----------------------------------------------------------


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
mcvard_res = team5.mcvard(x0, eps, u, f_huca_jivsa_test)

print_res(mcvard_name, mcvard_res)

# ----------------------------------------------------------


# ----------------------------------------------------------
# Тест методу Хука-Джівса
x = np.array([1, 3])

huca_jivsa_name: str = "Метод Хука-Дживса"
huca_jivsa_res = team5.huca_jivsa(x, f_huca_jivsa_test)

print_res(huca_jivsa_name, huca_jivsa_res)

# ----------------------------------------------------------


# ----------------------------------------------------------
# Тест методу хорд
a = -1
b = 0
eps = 10 ** -4

toxins_name: str = "Метод хорд"
toxins_res = team5.toxins(a, b, f_toxins_test, df_toxins_test)

print_res(toxins_name, toxins_res)

# ----------------------------------------------------------
