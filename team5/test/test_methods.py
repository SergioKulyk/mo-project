import numpy as np

f_gol_test = lambda x: x ** 3 - 27 * x + 5

f_tox_test = lambda x: x ** 2 + x + np.sin(x)
d_tox_test = lambda x: x ** 3 - 27 * x + 5

f_huc_test = lambda x: 4. * (x[0] - 5) ** 2 + (x[1] - 6) ** 2

f_mcv_test = lambda x: 4. * (x[0] - 5) ** 2 + (x[1] - 6) ** 2
g_mcv_test = lambda x: np.array([8. * (x[0] - 5), 2 * (x[1] - 6)])
h_mcv_test = lambda x: np.array([[8., 0], [0, 2.]])

f_fgd_test = lambda x: x[0] ** 2 + 4 * x[0] * x[1] + 17 * x[1] ** 2 + 5 * x[1]
g_fgd_test = lambda x: np.array([2 * x[0] + 4 * x[1], 4 * x[0] + 34 * x[1] + 5])

f_swr_test = lambda x: x[0] ** 2 + 4 * x[0] * x[1] + 17 * x[1] ** 2 + 5 * x[1]
