import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Melt_1
# from gwlfe import MeltPest


class TestMelt_1(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_Melt_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Melt_1.Melt_1_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec),
            Melt_1.Melt_1(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec), decimal=7)