## 0x07. Rotate 2D Matrix

For the “0. Rotate 2D Matrix” project, I was tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise.

This challenge requires a good understanding of matrix manipulation and in-place operations in Python.

Below are the key concepts needed in order to successfully complete this project.

### Concepts Needed:

1. Matrix Representation in Python:

Understanding how 2D matrices are represented using lists of lists in Python.

Accessing and modifying elements in a 2D matrix.

2. In-place Operations:

Performing operations on data without creating a copy of the data structure.

The importance of minimizing space complexity by modifying the matrix in place.

3. Matrix Transposition:

Understanding the concept of transposing a matrix (swapping rows and columns).

Implementing matrix transposition as a step in the rotation process.

4. Reversing Rows in a Matrix:

Manipulating rows of a matrix by reversing their order as part of the rotation process.

5. Nested Loops:

Using nested loops to iterate through 2D data structures like matrices.

Modifying elements within nested loops to achieve the desired rotation.

### Tasks

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):

Do not return anything. The matrix must be edited in-place.

You can assume the matrix will have 2 dimensions and will not be empty.

### Solution

1. Transpose the matrix:

This step converts rows to columns, which means element at position [i][j] in the matrix moves to position [j][i].

First, I iterate over all elements above the diagonal (i.e., where i < j), swapping matrix[i][j] with matrix[j][i].

Rows are converted into columns, but matrix is still "flipped" vertically, so the rows are reversed next.

2.Reverse each row:

After transposing, I reversed the order of elements in each row, using matrix[i].reverse() for each row.

This completes the 90-degree clockwise rotation.
