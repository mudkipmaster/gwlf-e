import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Grow_0
from gwlfe import enums


class TestGrow(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_Grow(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Grow_0.Grow_2(z.Grow_0),
            Grow_0.Grow_0(z.Grow_0)==enums.GROWING_SEASON, decimal=7)
