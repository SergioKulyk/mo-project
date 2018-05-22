import numpy as np

f_gol_test = lambda x: x ** 3 - 27 * x + 5

f_tox_test = lambda x: x ** 2 + x + np.sin(x)
d_tox_test = lambda x: x ** 3 - 27 * x + 5

f_huc_test = lambda x: 4. * (x[0] - 5) ** 2 + (x[1] - 6) ** 2

f_mcv_test = lambda x: 4. * (x[0] - 5) ** 2 + (x[1] - 6) ** 2

f_fgd_test = lambda x: x[0] ** 2 + 4 * x[0] * x[1] + 17 * x[1] ** 2 + 5 * x[1]

f_swr_test = lambda x: x[0] ** 2 + 4 * x[0] * x[1] + 17 * x[1] ** 2 + 5 * x[1]