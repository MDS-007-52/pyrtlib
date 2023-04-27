# -*- coding: utf-8 -*-

"""REFERENCES FOR MEASUREMENTS (freq in GHz, S in Hz*cm^2, W's,D's in GHZ/bar, X's & A dimensionless) updated Dec. 30, 2020.

    References
    ----------
    .. [1] M. Koshelev et al., JQSRT v.205, pp. 51-58 (2018)
    .. [2] V. Payne et al.,IEEE Trans. Geosci. Rem. Sens. v.46, pp.3601-3617 (2008)
    .. [3] G. Golubiatnikov, J. MOLEC. SPEC. vol. 230, pp.196-198 (2005)
    .. [4] M. Koshelev et al., J. Molec. Spec. v.241, pp.101-108 (2007)
    .. [5] J.-M. Colmont et al.,J. Molec. Spec. v.193, pp.233-243 (1999)
    .. [6] M. Tretyakov et al, JQSRT v.114 pp.109-121 (2013)
    .. [7] G. Golubiatnikov et al., JQSRT v.109, pp.1828-1833 (2008)
    .. [8] V. Podobedov et al., JQSRT v.87, pp. 377-385 (2004)
    .. [9] M. Koshelev, JQSRT v.112, pp.550-552 (2011)
    .. [10] M. Tretyakov, JQSRT v.328, pp.7-26 (2016)
    .. [11] D. Turner et al., IEEE Trans. Geosci. Rem. Sens. v.47 pp.3326-37 (2009), re-adjusted for new line par. Aug.22, 2022.
    .. [11] M. Koshelev et al. JQSRT doi:10.1016/j.jqsrt.2020.107472

    Other parameters from HITRAN2020.
"""
# code to import coefficient from .asc file
# import pandas as pd
# import numpy as np

# a = pd.read_table("h2o_sdlist.asc", sep=',',header=None, skiprows=1, nrows=19, usecols=range(0, 20))
# a = np.loadtxt("h2o_sdlist.asc", delimiter=',', skiprows=1, usecols=range(0, 20), max_rows=20)
# np.savetxt("/Users/slarosa/dev/pyrtlib/pyrtlib/lineshape/h2o_list_r22.txt", a)

import numpy as np
import os

PATH = os.path.dirname(os.path.abspath(__file__))
mtx = np.loadtxt(os.path.join(PATH, "h2o_list_r22.txt"))

ctr = np.array([300.0, 5.919e-10, 3.0, 1.416e-08, 7.5])

# # below is from abh2o_sd.f
# # read line parameters; units: ghz, hz*cm^2, mhz/mb
reftline = 296.0
fl = mtx[:, 1]
s1 = mtx[:, 2]
b2 = mtx[:, 3]
w0 = mtx[:, 4] / 1000.0
x = mtx[:, 5]
w0s = mtx[:, 6] / 1000.0
xs = mtx[:, 7]
sh = mtx[:, 8] / 1000.0
xh = mtx[:, 9]
shs = mtx[:, 10] / 1000.0
xhs = mtx[:, 11]
aair = mtx[:, 12]
aself = mtx[:, 13]
w2 = mtx[:, 14] / 1000.0
xw2 = mtx[:, 15]
w2s = mtx[:, 16] / 1000.0
xw2s = mtx[:, 17]
d2 = mtx[:, 18] / 1000.0
d2s = mtx[:, 19] / 1000.0

reftcon = ctr[0]
cf = ctr[1]
xcf = ctr[2]
cs = ctr[3]
xcs = ctr[4]

