# remember to import your libraries!
import numpy as np
import pandas as pd
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
    '''
    Reads in a csv file and gets the dimensions of tabular data.

    Parameters:
    -----------
    file_name = name of csv file to read in.

    Returns:
    --------
    A tuple indicating the number of rows and columns of the data.
    '''

    df = pd.read_csv(file_name, sep=',', header=None)

    return df.shape


def write_matrix_to_file(num_rows, num_columns, file_name):
    '''
    Writes a matrix of specified dimensions to a file.

    Parameters:
    -----------
    num_rows = integer;
               number of desired rows.
    num_columns = integer;
                  number of desired columns.
    file_name = string;
                name of file to write matrix to.

    Returns:
    --------
    This function returns the matrix produced.
    '''

    matrix = get_random_matrix(num_rows, num_columns)

    np.savetxt(file_name, matrix, delimiter=',')

    return matrix
