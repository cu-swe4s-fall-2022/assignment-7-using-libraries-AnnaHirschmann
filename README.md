# libraries

### **Description**
This project contains functions that allow the user to make a matrix of random floating point numbers, read a matrix from a file and get the dimensions, and write a matrix of random floating point numbers to a file. In addition, there is a file that produces three plots using the data from iris.data.

### **How to Use**
Run with `bash`.

**Functions in `data_processor.py`**
The following functions are in `data_processor.py`:
* `get_random_matrix`: This function takes two integer arguments (desired number of rows and columns) and returns a matrix of the desired dimensions containing floating point numbers in the range (0, 1].
* `get_file_dimensions`: Takes in the name of a file and returns the dimensions of tabular data stored in the file. 
* `write_matrix_to_file`: Takes in integer arguments for desired row and column dimensions as well as a file name, and writes a matrix of the desired dimensions filled with random floating point numbers to the specified file.

**Examples**
1. `get_random_matrix(5, 5)`: Produces a 5 by 5 matrix.
    a. If we wanted to write this matrix to a file, we could use `write_matrix_to_file(5, 5, file_name)` where file_name is the name of the file we wish to contain the matrix.
2. `get_file_dimensions(iris.data)`: returns (150, 5) indicating that this data is stored in a table with 150 rows and 5 columns.

**Information about `plotter.py`**
In this script, you will find code to produce three plots:
* A box plot that plots each of the four categories of data stored in `iris.data` (sepal length and width, petal length and width) vs. their length in centimeters.
* A scatter plot that compares petal width (cm) to petal length (cm) and colors the data according to the species of iris (iris-setosa, iris-versicolor, iris-virginica). 
* A multi-panel plot that plots the two above plots side-by-side.


### **How to Install**
This program runs with Python standard library, matplotlib, numpy, random, and pandas. Ensure all of these libraries are imported and installed on your machine to run this code.