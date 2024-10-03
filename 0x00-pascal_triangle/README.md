#### 0. Pascal's Triangle

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer


#### Solution Summary

1. Input Validation

Ensure n is a positive integer ; else raise error

2. Initialize Triangle

Create an empty list tri to store/hold the rows.

3. Generate rows

Loop through a range from 0 to n-1 to create each row, starting with 1.

For rows greater than 0, compute the inner values using the sum of appropriate elements from the previous row, and qppend these values to current row.


4. Return the completed triangle containing all rows up to n
