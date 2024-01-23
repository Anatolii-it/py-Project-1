import unittest

from func import *
class TestFunc(unittest.TestCase):
    def test_empty_list(self):
        my_list = []
        my_dob(my_list)
        assert True

    def test_positive_integers(self):
        my_list = [2, 3, 4]
        my_dob(my_list)
        assert True
    def test_negative_integers(self):
        my_list = [-2, -3, -4]
        my_dob(my_list)
        assert True

    def test_zeros(self):
        my_list = [0, 0, 0]
        my_dob(my_list)
        assert True