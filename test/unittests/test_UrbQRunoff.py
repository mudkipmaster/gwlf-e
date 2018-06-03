import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import UrbQRunoff


class TestUrbQRunoff(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_UrbQRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbQRunoff.UrbQRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                                    z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA),
            np.swapaxes(UrbQRunoff.UrbQRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                                    z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA),1,2)[:,:,z.NRur:]
            , decimal=7)