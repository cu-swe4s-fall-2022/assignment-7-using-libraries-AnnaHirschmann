# remember to import your libraries!
import numpy as np
import random

def get_random_matrix(num_rows, num_columns):
    '''
    Creates a matrix of random floating point numbers.
    
    Parameters:
    -----------
    num_rows = integer;
               the number of rows desired in the output matrix.
    
    num_columns = integer;
                  the number of columns desired in the output matrix.

    Returns:
    --------
    A matrix of size num_rows x num_columns (2 dimensional numpy array)
    that contains random floating point numbers from the range (0,1].
    '''
    
    return np.random.rand(num_rows, num_columns)

def get_file_dimensions(file_name):
    return (0,0)

def write_matrix_to_file(num_rows, num_columns, file_name):
    return None
