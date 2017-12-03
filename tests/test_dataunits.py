# This import fixes sys.path issues
from . import parentpath

import unittest
from octoprint_inkworks.dataunits import unit, celcius, ferenheit, related_unit_converter, compatible, convert_to_unit

class UnitsTest(unittest.TestCase):
    def test_ferenheit_celcius(self):
        self.assertEqual(convert_to_unit(ferenheit(212), celcius), 100)

    def test_celcius_ferenheit(self):
        self.assertEqual(convert_to_unit(celcius(100), ferenheit), 212.0)
