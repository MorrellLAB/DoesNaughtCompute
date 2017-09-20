#!/usr/bin/env python3

"""A top-down implementation of the merge sort with some extra information
Algorithm adopted from what's posted on the Wikipedia article"""

import sys
if sys.version_info.major is not 3:
    sys.exit("Please use Python 3 for this script")


#   A recurisve implementation of the merge-sort
def merge_sort(array):
    """Perform a merge sort on a list 'array'"""
    try:
        assert isinstance(array, list)
    except AssertionError:
        raise
    #   Stopping case for recursion
    if len(array) <= 1:
        return array
    #   Holding lists
    left = []
    right = []
    #   Split lists into odd- and even-index subsets of original list
    #   This is an arbitrary split
    for index, value in enumerate(array):
        if index % 2 == 1:
            left.append(value)
        else:
            right.append(value)
    #   Reduce the problem
    left_sort = merge_sort(array=left)
    right_sort = merge_sort(array=right)
    #   Return a merge of the reduced lists
    return merge(left=left_sort, right=right_sort)


#   A function to merge two lists and sort them
def merge(left, right):
    """Merge two lists: 'left' and 'right'"""
    try:
        assert isinstance(left, list)
        assert isinstance(right, list)
    except AssertionError:
        raise
    #   Create a holder list
    print("Left:", left, sep='\t', file=sys.stderr)
    print("Right:", right, sep='\t', file=sys.stderr)
    result = []
    #   Merge sort
    #   Runs while both lists have something in them
    #   At least one list will be exhausted
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]: # If the left is bigger than or equal to the right
            result.append(left.pop(0))
        else: # If the right is bigger than the left
            result.append(right.pop(0))
    #   Add any extras, at most one of these will run
    #   as the loop above will exhaust at least one list
    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    #   Return the result
    print("Merged:", result, sep='\t', file=sys.stderr)
    return result


#   If being run, then run
#   If imported, then __name__ is not '__main__'
if __name__ == '__main__':
    arr = [9, 4, 8, 3, 1, 2, 5]
    print("Initial list:", arr, sep='\t')
    print("Final list:", merge_sort(array=arr), sep='\t')
