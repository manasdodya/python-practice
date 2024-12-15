'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/insert-interval-1666733333

Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti. He wants to add a new interval newInterval= [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.

Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Examples:

Input: intervals = [[1,3], [4,5], [6,7], [8,10]], newInterval = [5,6]
Output: [[1,3], [4,7], [8,10]]
Explanation: The newInterval [5,6] overlaps with [4,5] and [6,7].

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,9]
Output: [[1,2], [3,10], [12,16]]
Explanation: The new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Constraints:
1 ≤ intervals.size() ≤  105
0 ≤ start[i], end[i] ≤ 109
'''
def insert_interval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    while i < n:
        # If current interval ends before newInterval starts
        if intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
        # If current interval starts after newInterval ends
        elif intervals[i][0] > newInterval[1]:
            result.append(newInterval)
            newInterval = intervals[i]  # Update newInterval to the current interval
        # If intervals overlap, merge them
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    # Add the last interval
    result.append(newInterval)
    return result

# Test examples
print(insert_interval([[1, 3], [4, 5], [6, 7], [8, 10]], [5, 6])) # Output [[1, 3], [4, 7], [8, 10]]
print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9])) #Output [[1, 2], [3, 10], [12, 16]]
print(insert_interval([], [5, 7])) #output [[5, 7]]
print(insert_interval([[1, 2], [3, 4]], [0, 5])) #output [[0, 5]]

'''
Algorithm

    Initialize Variables:
        Use a list result to store the final merged intervals.
        Traverse through the given intervals and decide where to place newInterval.

    Iterate Over Intervals:
        Case 1: If the current interval ends before newInterval starts, add it directly to result since they don't overlap.
        Case 2: If the current interval starts after newInterval ends, add newInterval to result (if not added already) and then add the current interval.
        Case 3: If there is an overlap, merge the intervals by updating the start and end of newInterval.

    Add Remaining Intervals:
        After processing all intervals, if newInterval is not added yet, append it to result.

    Return result:
        result contains all intervals merged appropriately.

Explanation of Example
Input:

intervals = [[1,3], [4,5], [6,7], [8,10]]
newInterval = [5,6]

Execution:

    Interval [1,3] ends before [5,6] starts → Add [1,3] to result.
    Interval [4,5] overlaps with [5,6] → Merge to [4,6].
    Interval [6,7] overlaps with [4,6] → Merge to [4,7].
    Interval [8,10] does not overlap → Add [4,7] (merged interval) and [8,10].

Output:

[[1,3], [4,7], [8,10]]

Time Complexity: O(n) The algorithm traverses the intervals list once, performing constant-time operations for each interval.

Space Complexity: O(n) The result list stores the merged intervals. If the input intervals and newInterval do not overlap, the space complexity is linear in the size of the input.

'''