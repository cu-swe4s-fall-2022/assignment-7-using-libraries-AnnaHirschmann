import unittest
import random
import numpy as np
import sys
import os
sys.path.append('../')
import data_processor  # nopep8


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_file_name = 'test_file.txt'
        f = open(cls.test_file_name, 'w')
        f.close()

    @classmethod
    def tearDownClass(cls):
        #  clears the random class initialized variables
        os.remove(cls.test_file_name)

    def test_get_random_matrix(self):
        num_rows = random.randint(1, 10)
        num_columns = random.randint(1, 10)
        matrix = data_processor.get_random_matrix(num_rows, num_columns)
        # checks that the returned matrix has the correct dimensions
        self.assertEqual(matrix.shape, (num_rows, num_columns))
        # checks that the element in the first row and column is a float
        self.assertIsInstance(matrix[0, 0], float)

    def test_get_file_dimensions(self):
        iris_dim = data_processor.get_file_dimensions('../iris.data')
        self.assertEqual(iris_dim, (150, 5))

    def test_write_matrix_to_file(self):
        num_rows = random.randint(1, 10)
        num_columns = random.randint(1, 10)

        matrix = data_processor.write_matrix_to_file(num_rows, num_columns,
                                                     self.test_file_name)

        self.assertEqual(matrix.shape, (num_rows, num_columns))


if __name__ == "__main__":
    unittest.main()
