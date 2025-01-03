'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/minimum-element-in-a-sorted-and-rotated-array3611

A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it. 

Examples:

Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element in the array.

Input: arr[] = [3, 1, 2]
Output: 1
Explanation: Here 1 is the minimum element.

Input: arr[] = [4, 2, 3]
Output: 2
Explanation: Here 2 is the minimum element.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 109
'''

def findMinimum(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare mid with the rightmost element
        if arr[mid] > arr[right]:
            # Minimum is in the right half
            left = mid + 1
        else:
            # Minimum is in the left half (including mid)
            right = mid

    # When left == right, we've found the minimum
    return arr[left]

# Examples
print(findMinimum([5, 6, 1, 2, 3, 4]))  # Output: 1
print(findMinimum([3, 1, 2]))           # Output: 1
print(findMinimum([4, 2, 3]))           # Output: 2

'''
Algorithm
    Key Observation:
        In a rotated sorted array, the smallest element is the pivot point where the rotation occurred. The pivot is the only element smaller than its predecessor.
        The array is split into two sorted subarrays around the pivot.

    Binary Search Logic:
        Compare the middle element with the rightmost element:
            If the middle element is greater than the rightmost element, the minimum lies in the right half.
            If the middle element is smaller than the rightmost element, the minimum lies in the left half (including the middle).

    Stop Condition:
        When the search range reduces to a single element, that element is the minimum.

Explanation of the Code

    Initialization:
        Start with two pointers, left = 0 and right = len(arr) - 1.

    Binary Search:
        Calculate the middle index as mid = (left + right) // 2.
        Compare arr[mid] with arr[right]:
            If arr[mid] > arr[right], the pivot (and thus the minimum) lies in the right half. Move left to mid + 1.
            If arr[mid] <= arr[right], the minimum lies in the left half. Move right to mid.

    Stop Condition:
        When left == right, the search range has reduced to a single element, which is the minimum.

Complexity Analysis

    Time Complexity: O(logn)
        The search range is halved at every step due to binary search.
    Space Complexity: O(1)
        No extra space is used.

'''