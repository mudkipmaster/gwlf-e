import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import NetSolidLoad


class TestNetSolidLoad(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NetSolidLoad(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NetSolidLoad.NetSolidLoad_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                        z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                        z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed,
                                        z.DisFract, z.FilterWidth, z.PctStrmBuf),
            NetSolidLoad.NetSolidLoad(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                        z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                        z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed,
                                        z.DisFract, z.FilterWidth, z.PctStrmBuf), decimal=7)
