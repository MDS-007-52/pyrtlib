# -*- coding: utf-8 -*-
"""
This file contains the line list used in absorption model.
"""

import numpy as np

from .absmodel import O2AbsModel, H2OAbsModel


class h2o_linelist:
    """This version correspond to 2018/07/23 package, where h2o_list.asc is dated July 16 2018

    REFERENCES FOR MEASUREMENTS (freq, W0,D in GHZ/bar, XW, XD, A, W2) updated Feb. 20, 2019
    REFERENCES FOR MEASUREMENTS (freq, W0air, W0self, Dair, Dself in GHZ/bar, Xair, Xself, XDair, XDself, W2)

    References
    ----------

        .. [1] M. Koshelev et al., JQSRT v.205, pp. 51-58 (2018)
        .. [2] M. Koshelev (private comm., 2019)
        .. [3] G. Golubiatnikov, J. MOLEC. SPEC. vol. 230, pp.196-198 (2005)
        .. [4] M. Koshelev et al., J. Molec. Spec. v.241, pp.101-108 (2007)
        .. [5] J.-M. Colmont et al.,J. Molec. Spec. v.193, pp.233-243 (1999)
        .. [6] M. Tretyakov et al, JQSRT v.114 pp.109-121 (2013)
        .. [7] G. Golubiatnikov et al., JQSRT v.109, pp.1828-1833 (2008)
        .. [8] V. Podobedov et al., JQSRT v.87, pp. 377-385 (2004)
        .. [9] M. Koshelev, JQSRT v.112, pp.550-552 (2011)
        .. [10] M. Tretyakov, JQSRT v.328, pp.7-26 (2016)
        .. [11] V. Payne et al.,IEEE Trans. Geosci. Rem. Sens. v.46, pp.3601-3617 (2008)
        .. [12] D. Turner et al., IEEE Trans. Geosci. Rem. Sens. v.47 pp.3326-37 (2009)

    Other parameters from HITRAN2016.
    Continuum re-adjusted for new line par. Mar. 20, 2019.
    """

    def __init__(self):
        """Initialize self. See help(type(self)) for accurate signature.

        Args:
            model (str): The absorption model used

        Raises:
            ValueError: [description]
        """
        model = H2OAbsModel.model

        # read the list of parameters
        # h2o_sdlist_r19
        # h2o_sdlist_r20
        # this is the same as h2o_sdlist_r19 but the two coefficients w2air w2self at 22.2 ghz
        # (which were missing in h2o_sdlist_r19)

        # 2019/03/18 - Nico: first created
        # blk = -9999; # blank
        blk = np.nan

        # molecule freq,GHz  S(296K)    B     W0air XWair W0self XWself  Dair  XDair  Dself XDself  Aair
        # Aself W2air W2self Refs. FL(i)     S1(i)    B2(i)   Wair  X(i)  Wself  Xs(i)   Sair  Xh(I)  Sself
        # Xhs(I) Aair Aself  W2   W2S (variable names in the code) Refs.

        self.mtx = np.vstack(
            [[11, 22.23508, 1.335e-14, 2.172, 2.74, 0.76, 13.63, 1.2, -0.033, 2.6, 0.814, blk, blk, blk, blk, blk],
             [11, 183.310087, 2.319e-12, 0.677, 3.028, 0.55, 15.01, 0.79, -0.073, 2.0, 0.112, 1.43, 0.0, 18.3, 0.406,
              1.499],
             [11, 321.22563, 7.657e-14, 6.262, 2.426, 0.73, 10.65, 0.54, -0.143, blk, 0.278, blk, blk, blk, blk, blk],
             [11, 325.152888, 2.721e-12, 1.561, 2.847, 0.64, 13.95, 0.74, -0.013, blk, 1.325, blk, blk, blk, blk, blk],
             [11, 380.197353, 2.477e-11, 1.062, 2.868, 0.54, 14.4, 0.89, -0.074, blk, 0.24, blk, blk, blk, blk, blk],
             [11, 439.150807, 2.137e-12, 3.643, 2.055, 0.69, 9.06, 0.52, 0.051, blk, 0.165, blk, blk, blk, blk, blk],
             [11, 443.018343, 4.44e-13, 5.116, 1.819, 0.7, 7.96, 0.5, 0.14, blk, -0.229, blk, blk, blk, blk, blk],
             [11, 448.001085, 2.588e-11, 1.424, 2.612, 0.7, 13.01, 0.67, -0.116, blk, -0.615, blk, blk, blk, blk, blk],
             [11, 470.888999, 8.196e-13, 3.645, 2.169, 0.73, 9.7, 0.65, 0.061, blk, -0.465, blk, blk, blk, blk, blk],
             [11, 474.689092, 3.268e-12, 2.411, 2.366, 0.71, 11.24, 0.64, -0.027, blk, -0.72, blk, blk, blk, blk, blk],
             [11, 488.490108, 6.628e-13, 2.89, 2.616, 0.75, 13.58, 0.72, -0.065, blk, -0.36, blk, blk, blk, blk, blk],
             [11, 556.935985, 1.57e-09, 0.161, 3.115, 0.75, 14.24, 1.0, 0.187, blk, -1.693, blk, blk, blk, blk, blk],
             [11, 620.700807, 1.7e-11, 2.423, 2.468, 0.79, 11.94, 0.75, 0.0, blk, 0.687, 0.92, blk, blk, blk, blk],
             [11, 658.006072, 9.033e-13, 7.921, 3.154, 0.73, 13.84, 1.0, 0.176, blk, -1.496, blk, blk, blk, blk, blk],
             [11, 752.033113, 1.035e-09, 0.402, 3.114, 0.77, 13.58, 0.84, 0.162, blk, -0.878, blk, blk, blk, blk, blk],
             [11, 916.171582, 4.275e-11, 1.461, 2.695, 0.79, 13.55, 0.48, 0.0, blk, 0.521, 0.47, blk, blk, blk, blk]])
        # continuum terms
        self.ctr = np.array([300.0, 5.929e-10, 3.0, 1.42e-08, 7.5])

        # below is from abh2o_sd.f
        # read line parameters; units: ghz, hz*cm^2, mhz/mb
        self.reftline = 296.0
        self.fl = self.mtx[:, 1]
        self.s1 = self.mtx[:, 2]
        self.b2 = self.mtx[:, 3]
        self.w0 = self.mtx[:, 4] / 1000.0
        self.x = self.mtx[:, 5]
        self.w0s = self.mtx[:, 6] / 1000.0
        self.xs = self.mtx[:, 7]
        self.sh = self.mtx[:, 8] / 1000.0
        self.xh = self.mtx[:, 9]
        self.shs = self.mtx[:, 10] / 1000.0
        self.xhs = self.mtx[:, 11]
        self.aair = self.mtx[:, 12]
        self.aself = self.mtx[:, 13]
        self.w2 = self.mtx[:, 14] / 1000.0
        self.w2s = self.mtx[:, 15] / 1000.0

        # replace non-existing shifting parameters with broadening parameters
        # indx = find(xh==blk); xh(indx) = x(indx);
        # indx = find(xhs==blk); xhs(indx) = xs(indx);
        indx = np.where(np.isnan(self.xh))
        self.xh[indx] = self.x[indx]
        indx = np.where(np.isnan(self.xhs))
        self.xhs[indx] = self.xs[indx]
        # replace non-existing aair aself parameters with zero (to be agreed with phil)
        # indx = find(aair==blk); aair(indx) = 0;
        # indx = find(aself==blk); aself(indx) = 0;
        indx = np.where(np.isnan(self.aair))
        self.aair[indx] = 0
        indx = np.where(np.isnan(self.aself))
        self.aself[indx] = 0
        # also for w2 and w2s (to be agreed with phil)
        # indx = find(w2==blk); w2(indx) = 0;
        # indx = find(w2s==blk); w2s(indx) = 0;
        indx = np.where(np.isnan(self.w2))
        self.w2[indx] = 0
        indx = np.where(np.isnan(self.w2s))
        self.w2s[indx] = 0
        # read continuum parameters; units: kelvin, 1/(km*mb^2*ghz^2)
        self.reftcon = self.ctr[0]
        self.cf = self.ctr[1]
        self.xcf = self.ctr[2]
        self.cs = self.ctr[3]
        self.xcs = self.ctr[4]


class o2_linelist:
    """Nico 2016/11/30
    Here I imported the code I got from P. Rosenkranz on 2016/08/10, adapting to RTE.

    NB: NL=49
    LINES ARE ARRANGED 1-,1+,...33-,33+ IN SPIN-ROTATION SPECTRUM;
    BY FREQUENCY IN SUBMM SPECTRUM.
    """

    def __init__(self):
        """Initialize self. See help(type(self)) for accurate signature.

        Args:
            model (str): The absorption model used

        Raises:
            ValueError: [description]
        """
        model = O2AbsModel.model

        # Nico F[GHz]
        self.f = np.array(
            [118.7503, 56.2648, 62.4863, 58.4466, 60.3061, 59.591, 59.1642, 60.4348, 58.3239, 61.1506, 57.6125, 61.8002,
             56.9682, 62.4112, 56.3634, 62.998, 55.7838, 63.5685, 55.2214, 64.1278, 54.6712, 64.6789, 54.13, 65.2241,
             53.5958, 65.7648, 53.0669, 66.3021, 52.5424, 66.8368, 52.0214, 67.3696, 51.5034, 67.9009, 50.9877, 68.431,
             50.4742, 68.9603, 233.9461, 368.4982, 401.7398, 424.763, 487.2493, 566.8956, 715.3929, 731.1866, 773.8395,
             834.1455, 895.071])
        # Nico S(T_0)[Hz*cm2]
        self.s300 = np.array(
            [2.906e-15, 7.957e-16, 2.444e-15, 2.194e-15, 3.301e-15, 3.243e-15, 3.664e-15, 3.834e-15, 3.588e-15,
             3.947e-15, 3.179e-15, 3.661e-15, 2.59e-15, 3.111e-15, 1.954e-15, 2.443e-15, 1.373e-15, 1.784e-15,
             9.013e-16, 1.217e-15, 5.545e-16, 7.766e-16, 3.201e-16, 4.651e-16, 1.738e-16, 2.619e-16, 8.88e-17,
             1.387e-16, 4.272e-17, 6.923e-17, 1.939e-17, 3.255e-17, 8.301e-18, 1.445e-17, 3.356e-18, 6.049e-18,
             1.28e-18, 2.394e-18, 3.287e-17, 6.463e-16, 1.334e-17, 7.049e-15, 3.011e-15, 1.797e-17, 1.826e-15,
             2.193e-17, 1.153e-14, 3.974e-15, 2.512e-17])
        # Nico (Elow+hf)/kT_0 [unitless]
        self.be = np.array(
            [0.01, 0.014, 0.083, 0.083, 0.207, 0.207, 0.387, 0.387, 0.621, 0.621, 0.91, 0.91, 1.255, 1.255, 1.654,
             1.654, 2.109, 2.109, 2.618, 2.618, 3.182, 3.182, 3.8, 3.8, 4.474, 4.474, 5.201, 5.201, 5.983, 5.983, 6.819,
             6.819, 7.709, 7.709, 8.653, 8.653, 9.651, 9.651, 0.019, 0.048, 0.045, 0.044, 0.049, 0.084, 0.145, 0.136,
             0.141, 0.145, 0.201])

        if model in ['rose18', 'rose19sd']:
            # Nico gamma(T_0) [MHZ/mb == GHz/bar]
            self.wb300 = 0.56
            self.x = 0.8
            self.w300 = np.array(
                [1.688, 1.703, 1.513, 1.491, 1.415, 1.408, 1.353, 1.339, 1.295, 1.292, 1.262, 1.263, 1.223, 1.217,
                 1.189,
                 1.174, 1.134, 1.134, 1.089, 1.088, 1.037, 1.038, 0.996, 0.996, 0.955, 0.955, 0.906, 0.906, 0.858,
                 0.858,
                 0.811, 0.811, 0.764, 0.764, 0.717, 0.717, 0.669, 0.669, 1.65, 1.64, 1.64, 1.64, 1.6, 1.6, 1.6, 1.6,
                 1.62,
                 1.47, 1.47])
            # nico y(t_0) [unitless]
            self.y300 = np.append(
                [-0.036, 0.2547, -0.3655, 0.5495, -0.5696, 0.6181, -0.4252, 0.3517, -0.1496, 0.043, 0.064, -0.1605,
                 0.2906, -0.373, 0.4169, -0.4819, 0.4963, -0.5481, 0.5512, -0.5931, 0.6212, -0.6558, 0.692, -0.7208,
                 0.7312, -0.755, 0.7555, -0.7751, 0.7914, -0.8073, 0.8307, -0.8431, 0.8676, -0.8761, 0.9046, -0.9092,
                 0.9416, -0.9423], np.tile(0.0, (1, 11)))
            # nico v(t_0) [unitless]
            self.v = np.append(
                [0.0079, -0.0978, 0.0844, -0.1273, 0.0699, -0.0776, 0.2309, -0.2825, 0.0436, -0.0584, 0.6056, -0.6619,
                 0.6451, -0.6759, 0.6547, -0.6675, 0.6135, -0.6139, 0.2952, -0.2895, 0.2654, -0.259, 0.375, -0.368,
                 0.5085, -0.5002, 0.6206, -0.6091, 0.6526, -0.6393, 0.664, -0.6475, 0.6729, -0.6545, 0.68, -0.66,
                 0.685, -0.665], np.tile(0.0, (1, 11)))
            # nico 2016/11/30 *********************************************************
        elif model in ['rose19']:
            # nico gamma(t_0) [mhz/mb == ghz/bar]
            self.wb300 = 0.56
            self.x = 0.754
            self.w300 = np.array(
                [1.685, 1.703, 1.513, 1.495, 1.433, 1.408, 1.353, 1.353, 1.303, 1.319, 1.262, 1.265, 1.238, 1.217,
                 1.207,
                 1.207, 1.137, 1.137, 1.101, 1.101, 1.037, 1.038, 0.996, 0.996, 0.955, 0.955, 0.906, 0.906, 0.858,
                 0.858,
                 0.811, 0.811, 0.764, 0.764, 0.717, 0.717, 0.669, 0.669, 1.65, 1.64, 1.64, 1.64, 1.6, 1.6, 1.6, 1.6,
                 1.62,
                 1.47, 1.47])

            self.y0 = np.append(
                [-0.041, 0.277, -0.373, 0.56, -0.573, 0.618, -0.366, 0.278, -0.089, -0.021, 0.0599, -0.152, 0.216,
                 -0.293, 0.374, -0.436, 0.491, -0.542, 0.571, -0.613, 0.636, -0.67, 0.69, -0.718, 0.74, -0.763,
                 0.788, -0.807, 0.834, -0.849, 0.876, -0.887, 0.915, -0.922, 0.95, -0.955, 0.987, -0.988],
                np.tile(0.0, (1, 11)))
            self.y1 = np.append(
                [0.0, 0.11, -0.009, 0.007, 0.049, -0.1, 0.26, -0.346, 0.364, -0.422, 0.315, -0.341, 0.483, -0.503,
                 0.598, -0.61, 0.63, -0.633, 0.613, -0.611, 0.57, -0.564, 0.58, -0.57, 0.61, -0.6, 0.64, -0.62, 0.65,
                 -0.64, 0.66, -0.64, 0.66, -0.64, 0.66, -0.64, 0.65, -0.63], np.tile(0.0, (1, 11)))

            self.g0 = np.append(
                [-0.000695, -0.09, -0.103, -0.239, -0.172, -0.171, 0.028, 0.15, 0.132, 0.17, 0.087, 0.069, 0.083,
                 0.068, 0.007, 0.016, -0.021, -0.066, -0.095, -0.116, -0.118, -0.14, -0.173, -0.186, -0.217,
                 -0.227, -0.234, -0.242, -0.266, -0.272, -0.301, -0.304, -0.334, -0.333, -0.362, -0.358, -0.348,
                 -0.344], np.tile(0.0, (1, 11)))
            self.g1 = np.append(
                [0.0, -0.042, 0.004, 0.025, 0.083, 0.167, 0.178, 0.223, 0.054, 0.003, 0.002, -0.044, -0.019, -0.054,
                 -0.177, -0.208, -0.294, -0.334, -0.368, -0.386, -0.374, -0.384, -0.387, -0.389, -0.423, -0.422,
                 -0.46, -0.46, -0.51, -0.5, -0.55, -0.53, -0.58, -0.56, -0.62, -0.59, -0.68, -0.65],
                np.tile(0.0, (1, 11)))

            self.dnu0 = np.append(
                [-0.00028, 0.00596, -0.0195, 0.032, -0.0475, 0.0541, -0.0232, 0.0155, 0.0007, -0.0086, -0.0026,
                 -0.0013, -0.0004, -0.002, 0.005, -0.007, 0.007, -0.008, 0.006, -0.007, 0.006, -0.006, 0.005,
                 -0.0049, 0.004, -0.0041, 0.0036, -0.0037, 0.0033, -0.0034, 0.0032, -0.0032, 0.003, -0.003, 0.0028,
                 -0.0029, 0.0029, -0.0029], np.tile(0.0, (1, 11)))
            self.dnu1 = np.append(
                [-0.00037, 0.0086, -0.013, 0.019, -0.026, 0.027, 0.005, -0.014, 0.012, -0.018, -0.015, 0.015, 0.003,
                 -0.004, 0.012, -0.013, 0.012, -0.012, 0.009, -0.009, 0.002, -0.002, 0.0005, -0.0005, 0.002, -0.002,
                 0.002, -0.002, 0.002, -0.002, 0.002, -0.002, 0.002, -0.002, 0.001, -0.001, 0.0004, -0.0004],
                np.tile(0.0, (1, 11)))
        else:
            raise ValueError('[Linelist] No model available with this name: {} . Sorry...'.format(model))
