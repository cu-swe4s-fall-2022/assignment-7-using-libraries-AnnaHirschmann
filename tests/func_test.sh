#!/bin/bash

set -e
set -u
set -o pipefail

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run basic_get_matrix python data.py --func_name 'get_random_matrix'
assert_exit_code 0


run basic_get_dim python data.py --func_name 'get_file_dimensions'
assert_in_stdout '(5, 5)'
assert_exit_code 0


#  run pycodestyle on python scripts
pycodestyle data_processor.py
pycodestyle data.py
pycodestyle plotter.py

#  run unit tests
python unit_tests.py

chmod -x func_test.sh