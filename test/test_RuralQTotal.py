import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import RuralQTotal


class TestRuralQTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_RuralQTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RuralQTotal.RuralQTotal_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.NUrb, z.AntMoist_0, z.Grow, z.Area),
            RuralQTotal.RuralQTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.NUrb, z.AntMoist_0, z.Grow, z.Area), decimal=7)