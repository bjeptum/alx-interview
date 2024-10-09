
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

### Solution Summary

- Start with the first box unlocked.
- I used Breadth-First Search (BFS) principles to check on all possible paths to unlock boxes starting from the first unlocked box.

BFS strategy is effective for exploring all possible states from a given starting point.


#### Steps

1) Initialization:
    
    -  Create a list to keep track of each unblocked box, starting with all boxes set to False(that is all are locked).

    - The first box, however,is set to True as it is always open

    - Create a queue 


#### Time Complexity

    `O(n + k)`

where:
    - n is the number of boxes (since we iterate through the list of boxes).
    
    - k is the total number of keys available across all boxes (since we process each key at most once).

#### Space Complexity

    `O(n)`

- The unlocked list has a size equal to the number of boxes.
- The queue in the worst case, may store all the indices of unlocked boxes.
