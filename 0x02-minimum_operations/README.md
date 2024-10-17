### 0x02. Minimum Operations

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: **Copy All** and **Paste**. Given a number `n`, this program calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

Write a method that calculates the minimum number of operations required to achieve exactly `n` `H` characters.


- Prototype:
```
def minOperations(n) -> int
```

- Returns an interger
- if n is impossible to achieve, return 0.

#### Must Know

For this project, one needs a solid understanding of the following concepts:

#### Dynamic Programming

Familiarity with dynamic programming can help in breaking down the problem into simpler subproblems and building up the solution.

- Dynamic Programming (GeeksforGeeks)

#### Prime Factorization

Understanding how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number n.

- Prime Factorization (Khan Academy)

#### Code Optimization

Knowing how to approach problems from an optimization perspective can be useful in finding the most efficient solution.

- How to optimize Python code

#### Greedy Algorithms

The problem can also be approached with greedy algorithms, choosing the best option at each step.

- Greedy Algorithms (GeeksforGeeks)

#### Basic Python Programming

Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.

- Python Functions (Python Official Documentation)


### Solution 

To reduce operations, we need to reduce the paste operations whenever it is possible which means performing the copy operations. 

Apply prime factorization to find the solution.

#### Steps:

1) Find the prime factors of n. Each prime factor represents an operation where you do A "Copy All" followed by "Paste" operations.

2) The total number of operations to achieve n will be the sum of its prime factors.

3) If n is 1, you do not need any operatioms (as you already have 'H'). If n is less than 1, it is impossible to achieve returning 0.

4) Iterate through the potential factors starting from 2 up.  The inner loop divides n by i as long i is a factor and adds the factor to the operation count.

5) Sum the factors found, each time it is found to the total number of operations.
