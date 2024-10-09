#!/usr/bin/python3
""" Lockboxes Module."""
def canUnlockAll(boxes):
    """ Determine if all boxes can be opened."""
    # Track unlocked boxes
    unlocked = [False] * len(boxes)
    # Start with first block as unlocked
    unlocked[0] = True

    # Create a queue starting with the first box
    queue = [0]

    while queue:
        current_box = queue.pop(0)  # Get next box

        # Check the keys inside the current box

        for key in boxes[current_box]:
            # If the key opens a box and that box is still locked
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # Unlock that box
                queue.append(key)  # Add box to queue to check later

        # Check if we unlocked all boxes
    return all(unlocked)
