import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Loads import NGLoadN


class TestNGLoadN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_NGLoadN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLoadN.NGLoadN_2(),
            NGLoadN.NGLoadN(), decimal=7)