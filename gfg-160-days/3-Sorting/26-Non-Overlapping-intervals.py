'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/non-overlapping-intervals

Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Examples:

Input: intervals[][] = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals[][] = [[1, 3], [1, 3], [1, 3]]
Output: 2
Explanation: You need to remove two [1, 3] to make the rest of the intervals non-overlapping.

Input: intervals[][] = [[1, 2], [5, 10], [18, 35], [40, 45]]
Output: 0
Explanation: All ranges are already non overlapping.

Constraints:
1 ≤ intervals.size() ≤  105
|intervalsi| == 2
0 ≤ starti < endi <=5*104

'''

def erase_overlap_intervals(intervals):
    # Sort intervals by their end time
    intervals.sort(key=lambda x: x[1])
    
    # Initialize variables
    prev_end = float('-inf')
    removals = 0
    
    for start, end in intervals:
        # Check for overlap
        if start >= prev_end:
            prev_end = end  # Update end time for the current interval
        else:
            removals += 1  # Increment removals for overlapping interval
    
    return removals


# Test cases
print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])) # Output = 1
print(erase_overlap_intervals([[1, 3], [1, 3], [1, 3]])) # output = 2
print(erase_overlap_intervals([[1, 2], [5, 10], [18, 35], [40, 45]])) # output = 0

examples = [
    [[1, 2], [2, 3], [3, 4], [1, 3]],
    [[1, 3], [1, 3], [1, 3]],
    [[1, 2], [5, 10], [18, 35], [40, 45]]
]

for i, intervals in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: {intervals}")
    print(f"  Output: {erase_overlap_intervals(intervals)}")
    print()

'''
Algorithm

    Sort Intervals:
        Sort the intervals based on their end times in ascending order. This ensures that the intervals with the earliest end times are considered first, minimizing overlaps.

    Iterate Through Intervals:
        Initialize prev_end to track the end time of the last included interval.
        Initialize removals to count the number of removed intervals.
        Traverse the intervals:
            If the current interval's start time is greater than or equal to prev_end, include it and update prev_end to the current interval's end time.
            Otherwise, increment removals because the current interval overlaps with the previous one.

    Return removals:
        The count of removed intervals will ensure that the remaining intervals are non-overlapping.

Explanation of Example
Input:

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

Execution:

    Sort intervals by end times: [[1, 2], [2, 3], [1, 3], [3, 4]].
    Start traversing:
        Include [1, 2], update prev_end = 2.
        Include [2, 3], update prev_end = 3.
        Skip [1, 3] because 1 < prev_end, increment removals = 1.
        Include [3, 4], update prev_end = 4.
    Output: 1.

Time Complexity: O(n log n)
    Sorting the intervals takes O(nlogn).
    Traversing the sorted list takes OO(n).
    Total complexity: O(nlogn).

Space Complexity: O(1) Sorting is in-place and no additional data structures are used.
'''