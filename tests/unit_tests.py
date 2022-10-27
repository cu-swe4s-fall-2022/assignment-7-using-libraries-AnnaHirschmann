from os import path
import sys
import unittest
import random
sys.path.append("..") # no pep8
import data_processor as dp

class TestUtils(unittest.TestCase):
    def test_get_random_matrix(self):
        num_rows = random.randint(1, 10)
        num_cols = random.randint(1, 10)
        matrix = dp.get_random_matrix(num_rows, num_columns)
        self.assertEqual(matrix.shape, (num_rows, num_columns))