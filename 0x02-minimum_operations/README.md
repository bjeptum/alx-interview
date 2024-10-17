### 0x02. Minimum Operations

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: **Copy All** and **Paste**. Given a number `n`, this program calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

Write a method that calculates the minimum number of operations required to achieve exactly `n` `H` characters.


- Prototype:
```
def minOperations(n) -> int
```

- Returns an interger
- if n is impossible to achieve, return 0.


### Solution 

To reduce operations, we need to reduce the paste operations whenever it is possible which means performing the copy operations. 

Apply prime factorization to find the solution.

#### Steps:

1) Find the prime factors of n. Each prime factor represents an operation where you do A "Copy All" followed by "Paste" operations.

2) The total number of operations to achieve n will be the sum of its prime factors.


3) If n is !, you do not need any operatioms (as you already have 'H'). If n is less thamn 1, it is impossible to achieve returning 0.

4) Iterate through the potential factors starting from 2 up to the square root of n.  The inner loop divides n by i as long i is a factor and adds the factor to the operation count.

5) Sum the factors found, each time it is found to the total number of operations.

6) If after all the divisions n is still greater tha 1, n itself is a prime factor and we add it to the sum of factors.
