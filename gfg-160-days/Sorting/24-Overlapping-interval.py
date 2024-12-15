'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/overlapping-intervals--170633

Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

Examples:

Input: arr[][] = [[1,3],[2,4],[6,8],[9,10]]
Output: [[1,4], [6,8], [9,10]]
Explanation: In the given intervals we have only two overlapping intervals here, [1,3] and [2,4] which on merging will become [1,4]. Therefore we will return [[1,4], [6,8], [9,10]].

Input: arr[][] = [[6,8],[1,9],[2,4],[4,7]]
Output: [[1,9]]
Explanation: In the given intervals all the intervals overlap with the interval [1,9]. Therefore we will return [1,9].

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ starti ≤ endi ≤ 105

'''

def merge_intervals_in_place(arr):
    # Sort intervals by their starting times
    arr.sort(key=lambda x: x[0])

    # Index to write the next merged interval
    write_index = 0

    for i in range(1, len(arr)):
        # Check for overlap
        if arr[write_index][1] >= arr[i][0]:
            # Merge intervals
            arr[write_index][1] = max(arr[write_index][1], arr[i][1])
        else:
            # Move to the next position
            write_index += 1
            arr[write_index] = arr[i]

    # Return merged intervals up to the write_index
    return arr[:write_index + 1]

# Test cases
print(merge_intervals_in_place([[1, 3], [2, 4], [6, 8], [9, 10]])) # Output [[1, 4], [6, 8], [9, 10]]
print(merge_intervals_in_place([[6, 8], [1, 9], [2, 4], [4, 7]])) # Output [[1, 9]]
print(merge_intervals_in_place([[1, 4], [4, 5]])) # Output [[1, 5]]
print(merge_intervals_in_place([[1, 4], [2, 3]])) # Output [[1, 4]]
print(merge_intervals_in_place([[1, 4], [5, 6]])) # Output [[1, 4], [5, 6]]

'''
Algorithm 

    Sort Intervals:
        Sort the intervals array in place based on the start times.

    Merge In Place:
        Use a pointer (write_index) to keep track of the position in the array where the next merged interval should be written.
        Compare each interval with the interval at write_index to determine if they overlap:
            If they do, update the end of the interval at write_index.
            If they don't, move write_index forward and overwrite it with the current interval.

    Truncate the Array:
        After merging, the intervals from write_index + 1 onward are unnecessary.

    Return the Result:
        Return the intervals up to write_index + 1.

Explanation of Example
Input: [[6, 8], [1, 9], [2, 4], [4, 7]]

    Sort the intervals:
        Sorted intervals: [[1, 9], [2, 4], [4, 7], [6, 8]].

    Merge step-by-step:
        write_index = 0, Start with arr[0] = [1, 9].
        Compare arr[0] with arr[1] ([2, 4]): Overlaps → Merge → Update arr[0] = [1, 9].
        Compare arr[0] with arr[2] ([4, 7]): Overlaps → Merge → Update arr[0] = [1, 9].
        Compare arr[0] with arr[3] ([6, 8]): Overlaps → Merge → Update arr[0] = [1, 9].

    Result:
        Final merged intervals: [[1, 9]].


Time Complexity:

    Sorting: O(nlogn).
    Merging: O(n).
    Overall: O(nlogn).

Space Complexity:

    Sorting is in place.
    Merging is done in place with no additional space.
    Overall: O(1).

'''