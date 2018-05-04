import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Loads import InitNgN


class TestInitNgN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_InitNgN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            InitNgN.InitNgN_2(),
            InitNgN.InitNgN(), decimal=7)