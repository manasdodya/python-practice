'''
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-bonus-problems/problem/attend-all-meetings

Given an array arr[][] such that arr[i][0] is the starting time of ith meeting and arr[i][1] is the ending time of ith meeting, the task is to check if it is possible for a person to attend all the meetings such that he can attend only one meeting at a particular time.

Note: A person can attend a meeting if its starting time is greater than or equal to the previous meeting's ending time.

Examples:

Input: arr[][] = [[1, 4], [10, 15], [7, 10]]
Output: true
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings.

Input: arr[][] = [[2, 4], [9, 12], [6, 10]]
Output: false
Explanation: It is not possible to attend the second and third meetings simultaneously.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 2*106
'''

def can_attend_all_meetings(arr):
    # Sort meetings by their start times
    arr.sort(key=lambda x: x[0])  # O(n log n) for sorting

    # Check for overlaps
    for i in range(1, len(arr)):
        # If the current meeting starts before the previous meeting ends
        if arr[i][0] < arr[i - 1][1]:
            return False

    return True


# Example Usage
if __name__ == "__main__":
    arr1 = [[1, 4], [10, 15], [7, 10]]
    print(can_attend_all_meetings(arr1))  # Output: True

    arr2 = [[2, 4], [9, 12], [6, 10]]
    print(can_attend_all_meetings(arr2))  # Output: False

'''
Algorithm

Sort the Meetings by Start Time:

    First, sort the array of meeting intervals based on their start times. Sorting has a time complexity of O(nlogn).

Check for Overlapping Meetings:

    Traverse the sorted meetings. For each meeting, check if the start time of the current meeting is less than the end time of the previous meeting. If so, return false.

Output Result:

    If no overlap is found after checking all meetings, return true.

Explanation

    Sorting:
        The meetings are sorted by their starting times so that they are in chronological order. This ensures we can simply compare adjacent meetings for overlaps.

    Overlap Check:
        After sorting, traverse the meetings and check if the start time of the current meeting is less than the end time of the previous meeting. If this condition holds true, it means the meetings overlap, and the person cannot attend both.

Complexity Analysis

    Time Complexity:
        Sorting the meetings: O(nlogn)
        Iterating through the meetings to check overlaps: O(n)O(n)
        Total: O(nlogn)

    Space Complexity:
        Since sorting can be done in place, the space complexity is O(1)O(1), aside from input storage.

'''