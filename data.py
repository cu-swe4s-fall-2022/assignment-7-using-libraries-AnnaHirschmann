import random
import data_processor
import sys
import argparse

parser = argparse.ArgumentParser(description="Run any of data_processor functions.")

parser.add_argument('--func_name',
                    type=str,
                    help="Which function do you want to run?\
                    get_random_matrix or get_file_dimensions?",
                    required=True)

args = parser.parse_args()


def main():
    num_rows = 5
    num_columns = 5
    
    if args.func_name == 'get_random_matrix':
        matrix = get_random_matrix(num_rows, num_columns)

    else:
        dim = get_file_dimensions('../iris.data')
        print(dim)

if __name__ == '__main__':
    main()
    