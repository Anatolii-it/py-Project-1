import unittest

from main import my_minimum


class TestFunc(unittest.TestCase):
    def test_positive_integers(self):
        assert my_minimum([9, 2, 7, 4, 5]) == 2
    def test_negative_integers(self):
        assert my_minimum([-9, -2, -7, -4, -5]) == -9
    def test_mixed_integers(self):
        assert my_minimum([-9, 2, -7, 4, -5]) == -9
    def test_floats(self):
        assert my_minimum([9.5, 2.3, 7.1, 4.9, 5.7]) == 2.3
