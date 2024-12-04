## 0x09. Island Perimeter

The "0. Island Perimeter" project is designed to test my knowledge of algorithms, data structures (specifically matrices or 2D lists), and logic to solve a geometric problem within a grid context. The goal of the project is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers.

### Task

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid.

### Constraints

- Each cell in the grid is square with a side length of `1`.
- Cells are connected horizontally and vertically (but not diagonally).
- The grid is rectangular, with its width and height not exceeding `100`.
- The grid is completely surrounded by water.
- There is only one island (or no island).
- The island does not contain "lakes" (water inside the island that isn't connected to the surrounding water).

### Concepts Needed:

    1. 2D Arrays (Matrices):

Accessing and iterating over elements in a 2D array.
Understanding how to navigate through adjacent cells (horizontally and vertically).

    2. Conditional Logic:

Applying conditions to determine whether a cell contributes to the perimeter of the island.
    3. Counting Techniques:

Developing a method to count the edges that contribute to the island’s perimeter.

    4. Problem-Solving Strategies:

Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

    5. Python Programming:

Nested loops for iterating over grid cells.
Conditional statements to check the status of adjacent cells.

