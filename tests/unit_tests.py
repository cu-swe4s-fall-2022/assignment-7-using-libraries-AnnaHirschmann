import unittest
import random
import numpy as np
import sys
sys.path.append('../')
import data_processor  # nopep8

class TestUtils(unittest.TestCase):
    def test_get_random_matrix(self):
        num_rows = random.randint(1, 10)
        num_columns = random.randint(1, 10)
        matrix = data_processor.get_random_matrix(num_rows, num_columns)
        self.assertEqual(matrix.shape, (num_rows, num_columns))
        
if __name__ == "__main__":
    unittest.main()