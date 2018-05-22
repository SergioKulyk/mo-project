from team5.lib5.Team5 import *
from team5.test.test_methods import *


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

gol_name = "Метод золотого перерізу"
tox_name = "Метод хорд"
huc_name = "Метод Хука-Дживса"
fgd_name = "Найшвідшого градієнтного спуску"
mcv_name = "Метод Макварада"
swr_name = "Метод рою частинок"

# Створюємо обєкт класа Team5
team5 = Team5()

# ----------------------------------------------------------
# Тест методу золотого перерізу
a = -4
b = 4

golden_section_res = team5.golden_section(a, b, f_gol_test)

print_res(gol_name, golden_section_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу хорд
a = -1
b = 0
eps = 10 ** -4

toxins_res = team5.toxins(a, b, f_tox_test, d_tox_test)

print_res(tox_name, toxins_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу Хука-Дживса
x = np.array([1, 3])

huca_jivsa_res = team5.huca_jivsa(x, f_huc_test)

print_res(huc_name, huca_jivsa_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу найшвідшого градієнтного спуску
x = np.array([0., 1.])

faster_gradient_descent_res = team5.faster_gradient_descent(x, f_fgd_test)

print_res(fgd_name, faster_gradient_descent_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу Макварада
x0 = np.array([8., 9.])

mcvard_res = team5.mcvard(x0, f_huc_test)

print_res(mcv_name, mcvard_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу рою частинок
s = 40
d = 2

swarm_parties_res = team5.swarm_parties(s, d, f_swr_test)

print_res(swr_name, swarm_parties_res)
# ----------------------------------------------------------
