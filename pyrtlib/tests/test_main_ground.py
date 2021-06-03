import os
# from pathlib import Path
from unittest import TestCase

import numpy as np
import pandas as pd
from numpy.testing import assert_allclose
from pyrtlib.atmp import AtmosphericProfiles as atmp
from pyrtlib.main import BTCloudRTE
from pyrtlib.absmodel import H2OAbsModel
from pyrtlib.apiwebservices import ERA5Reanalysis
from pyrtlib.utils import ppmv2gkg, mr2rh, import_lineshape

# TEST_DIR = Path(__file__).parent
# DATA_DIR = os.path.join(TEST_DIR, 'data')
THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class Test(TestCase):

    # @pytest.mark.datafiles(DATA_DIR)
    def test_pyrtlib_ground_rose19sd(self):
        z, p, _, t, md = atmp.gl_atm(atmp.TROPICAL)

        gkg = ppmv2gkg(md[:, atmp.H2O], atmp.H2O)
        rh = mr2rh(p, t, gkg)[0] / 100

        ang = np.array([90.])
        frq = np.arange(20, 201, 1)

        rte = BTCloudRTE(z, p, t, rh, frq, ang)
        rte.satellite = False
        rte.init_absmdl('rose19sd')
        df = rte.execute()

        df_expected = pd.read_csv(os.path.join(THIS_DIR, "data", "tb_tot_ground_ros03_19sd_21sdera5.csv"))
        assert_allclose(df.tbtotal, df_expected.ros19sd, atol=0)

    # @pytest.mark.datafiles(DATA_DIR)
    # @pytest.mark.skip(reason="rose03 not completly implemented yet")
    def test_pyrtlib_ground_rose03(self):
        z, p, _, t, md = atmp.gl_atm(atmp.TROPICAL)

        gkg = ppmv2gkg(md[:, atmp.H2O], atmp.H2O)
        rh = mr2rh(p, t, gkg)[0] / 100

        ang = np.array([90.])
        frq = np.arange(20, 201, 1)

        rte = BTCloudRTE(z, p, t, rh, frq, ang)
        rte.satellite = False
        rte.init_absmdl('rose03')
        df = rte.execute()

        df_expected = pd.read_csv(os.path.join(THIS_DIR, "data", "tb_tot_ground_ros03_19sd_21sdera5.csv"))
        assert_allclose(df.tbtotal, df_expected.ros03, atol=0)

    def test_pyrtlib_ground_rose21sd_ERA5(self):
        lonlat = (15.724447, 40.601019)
        nc_file = os.path.join(THIS_DIR, "data", "era5_reanalysis-2019-06-25T12:00:00.nc")
        df_era5 = ERA5Reanalysis.read_data(nc_file, lonlat)

        mdl = 'rose21sd'
        ang = np.array([90.])
        frq = np.arange(20, 201, 1)
        nf = len(frq)

        rte = BTCloudRTE(df_era5.z.values, df_era5.p.values, df_era5.t.values, df_era5.rh.values, frq, ang)
        rte.satellite = False
        rte.init_absmdl('rose20')
        H2OAbsModel.model = 'rose21sd'
        H2OAbsModel.h2oll = import_lineshape('h2oll_{}'.format(H2OAbsModel.model))
        df = rte.execute()

        df_expected = pd.read_csv(os.path.join(THIS_DIR, "data", "tb_tot_ground_ros03_19sd_21sdera5.csv"))
        assert_allclose(df.tbtotal, df_expected.rose21sd_era5, atol=0)
