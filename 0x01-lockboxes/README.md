
### 0x01. Lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return Falsei

## Must Know

For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

## Concepts Needed

##### 1. Lists and List Manipulation
- Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
- [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/introduction.html#lists)

##### 2. Graph Theory Basics
- Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
- [Graph Theory (Khan Academy)](https://www.khanacademy.org/math/discrete-math)

##### 3. Algorithmic Complexity
- Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
- [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-big-oh-notation/)

##### 4. Recursion
- Some solutions might require a recursive approach to traverse through the boxes and keys.
- [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

##### 5. Queue and Stack
- Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
- [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/stack-in-python/)

##### 6. Set Operations
- Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
- [Python Sets (Python Official Documentation)](https://docs.python.org/3/library/stdtypes.html#set)


### Solution Summary

- Start with the first box unlocked.
- I used Breadth-First Search (BFS) principles to check on all possible paths to unlock boxes starting from the first unlocked box.

BFS strategy is effective for exploring all possible states from a given starting point.


#### Steps

1) Initialization:
    
    -  Create a list to keep track of each unblocked box, starting with all boxes set to False(that is all are locked).

    - The first box, however,is set to True as it is always open.

    - Create a queue initialized with the index of first box(0). This will help with processing each box in the order they are encountered:

        a) Pop the first element from the queue, which gives the index of the current box being examined.

        b) For each key found in the current_box, check if the key can unlock another box:
        
        - The condition key < len(boxes) ensures the key corresponds to a valid box index.
        - The condition not unlocked[key] checks whether that box is currently locked. If it is locked:
            - Set unlocked[key] to True, marking the box as unlocked.
            - Add the index of the unlocked box to the queue so as to check its contents in subsequent iterations.

2) Process the Queue

 - Enter a while loop that continues until the queue is empty.

3) Check if all boxes are unlocked. Return True if all elements in the list are True(all boxes can be opened), else return False.


#### Time Complexity

    `O(n + k)`

where:

    - n is the number of boxes (since we iterate through the list of boxes).
    
    - k is the total number of keys available across all boxes (since we process each key at most once).

#### Space Complexity

    `O(n)`

- The unlocked list has a size equal to the number of boxes.
- The queue in the worst case, may store all the indices of unlocked boxes.
