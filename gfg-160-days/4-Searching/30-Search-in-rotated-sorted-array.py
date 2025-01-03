'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/search-in-a-rotated-array4618

Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found.

Examples :

Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
Output: 8
Explanation: 3 is found at index 8.

Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: There is no element that has value 6.

Input: arr[] = [33, 42, 72, 99], key = 42
Output: 1
Explanation: 42 is found at index 1.

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106
1 ≤ key ≤ 106
'''
def searchInRotatedArray(arr, key):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # If key is found at mid
        if arr[mid] == key:
            return mid

        # Check if the left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= key < arr[mid]:  # Key is in the left half
                right = mid - 1
            else:  # Key is in the right half
                left = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < key <= arr[right]:  # Key is in the right half
                left = mid + 1
            else:  # Key is in the left half
                right = mid - 1

    # Key not found
    return -1

# Examples
print(searchInRotatedArray([5, 6, 7, 8, 9, 10, 1, 2, 3], 3))  # Output: 8
print(searchInRotatedArray([3, 5, 1, 2], 6))                 # Output: -1
print(searchInRotatedArray([33, 42, 72, 99], 42))            # Output: 1

'''
Algorithm

    Binary Search with Modification:
        Divide the array into two halves using the middle index.
        Determine which half is sorted:
            If the left half is sorted, check if the target lies within the range of this half. If so, search in this half; otherwise, search in the other half.
            If the right half is sorted, check if the target lies within the range of this half. If so, search in this half; otherwise, search in the other half.

    Stop Condition:
        If the key is found, return its index.
        If the search range is exhausted (left > right), return -1.

    Time Complexity:
        The binary search ensures a time complexity of O(logn).

Explanation of the Code

    Initialization:
        Start with left = 0 and right = len(arr) - 1.

    Binary Search:
        Calculate the middle index as mid = (left + right) // 2.
        If arr[mid] == key, return mid.
        Determine which half of the array is sorted:
            Left half sorted: arr[left] <= arr[mid]
                Check if key is in the range [arr[left], arr[mid]).
            Right half sorted: Otherwise, the right half is sorted.
                Check if key is in the range (arr[mid], arr[right]].

    Update Pointers:
        If the key is in the sorted half, update left or right to narrow the search.

    Key Not Found:
        If the loop ends, return -1.

Examples with Step-by-Step Explanation
Example 1

Input:

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3

    Initial Range: left = 0, right = 8, mid = 4
        arr[mid] = 9
        Left half [5, 6, 7, 8, 9] is sorted, but 3 is not in this range.
        Update left = 5.

    New Range: left = 5, right = 8, mid = 6
        arr[mid] = 1
        Right half [1, 2, 3] is sorted, and 3 is in this range.
        Update left = 7.

    New Range: left = 7, right = 8, mid = 7
        arr[mid] = 2
        Update left = 8.

    Final Check: mid = 8
        arr[mid] = 3, return 8.

Output: 8
'''