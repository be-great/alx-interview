#!/usr/bin/python3
"""
0. Lockboxes
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened.
    """
    opened = set([0])
    keys = boxes[0]
    # init key with first box keys
    queue = keys[:]
    while queue:
        key = queue.pop()
        if key < len(boxes) and key not in opened:
            opened.add(key)
            queue.extend(boxes[key])
    return len(opened) == len(boxes)
