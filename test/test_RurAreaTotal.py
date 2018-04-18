import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import RurAreaTotal


class TestRurAreaTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_RurAreaTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurAreaTotal.RurAreaTotal_2(),
            RurAreaTotal.RurAreaTotal(), decimal=7)