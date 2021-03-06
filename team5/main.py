from team5.lib5.Team5 import *
from team5.test.test_methods import *
from team5.utilities.Utilities import *

# ----------------------------------------------------------
# Тест методу золотого перерізу
a = -4
b = 4

golden_section_res = Team5.golden_section(a, b, f_gol_test)

Utilities.print_res(Utilities.gol_name, golden_section_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу хорд
a = -1
b = 0
eps = 10 ** -4

toxins_res = Team5.toxins(a, b, f_tox_test, d_tox_test)

Utilities.print_res(Utilities.tox_name, toxins_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу Хука-Дживса
x = np.array([1, 3])

huca_jivsa_res = Team5.huca_jivsa(x, f_huc_test)

Utilities.print_res(Utilities.huc_name, huca_jivsa_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу найшвідшого градієнтного спуску
x = np.array([0., 1.])

faster_gradient_descent_res = Team5.faster_gradient_descent(x, f_fgd_test, g_fgd_test)

Utilities.print_res(Utilities.fgd_name, faster_gradient_descent_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу Макварада
x0 = np.array([8., 9.])

mcvard_res = Team5.mcvard(x0, f_huc_test, g_mcv_test, h_mcv_test)

Utilities.print_res(Utilities.mcv_name, mcvard_res)
# ----------------------------------------------------------

# ----------------------------------------------------------
# Тест методу рою частинок
s = 40
d = 2

swarm_parties_res = Team5.swarm_parties(s, d, f_swr_test)

Utilities.print_res(Utilities.swr_name, swarm_parties_res)
# ----------------------------------------------------------
