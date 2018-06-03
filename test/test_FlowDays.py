import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import FlowDays


class TestFlowDays(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    # def test_FlowDays(self):
    #     z = self.z
    #     np.testing.assert_array_almost_equal(
    #         FlowDays.FlowDays_2(),
    #         FlowDays.FlowDays(), decimal=7)