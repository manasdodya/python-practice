'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/subarray-with-given-sum-1587115621

Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.

Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.

Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 103
0 <= target <= 109
'''

def find_subarray_with_sum(arr, target):
    n = len(arr)
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]  # Add the current element to the sum
        
        # Shrink the window while the sum is greater than the target
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1
        
        # Check if the current window's sum equals the target
        if current_sum == target:
            return [start + 1, end + 1]  # Return 1-based indices

    # If no subarray is found, return [-1]
    return [-1]

# Example Usage
arr1 = [1, 2, 3, 7, 5]
target1 = 12
print("Output for arr1:", find_subarray_with_sum(arr1, target1))  # Output: [2, 4]

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 15
print("Output for arr2:", find_subarray_with_sum(arr2, target2))  # Output: [1, 5]

arr3 = [5, 3, 4]
target3 = 2
print("Output for arr3:", find_subarray_with_sum(arr3, target3))  # Output: [-1]


'''
Algorithm

The problem can be solved efficiently using a sliding window (two-pointer) approach:

    Initialize Variables:
        current_sum to store the sum of the current window (initially 0).
        Two pointers: start (beginning of the window) and end (end of the window).

    Iterate Through the Array:
        Add arr[end] to current_sum as the window expands by moving end.
        If current_sum exceeds target, shrink the window from the left by incrementing start and subtracting arr[start] from current_sum.

    Check for Subarray:
        If current_sum equals target, return [start + 1, end + 1] (1-based indices).
        Continue until the entire array is traversed.

    Return -1:
        If no such subarray is found, return [-1].

Example Walkthrough
Example 1

Input:
arr = [1, 2, 3, 7, 5], target = 12

Steps:

    end = 0, current_sum = 1
    end = 1, current_sum = 3
    end = 2, current_sum = 6
    end = 3, current_sum = 13 (exceeds target) → Shrink window (start = 1, current_sum = 12).
        Match Found: Subarray [2, 4] (1-based indices).

Output: [2, 4]
Example 2

Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15

Steps:

    end = 0 to 4: Increment current_sum = 15.
        Match Found: Subarray [1, 5].

Output: [1, 5]
Example 3

Input:
arr = [5, 3, 4], target = 2

Steps:

    Traverse entire array without finding a subarray.

Output: [-1]
Complexity Analysis

    Time Complexity:
        The array is traversed once, and the start pointer moves at most nn times.
        Overall: O(n).

    Space Complexity:
        No additional data structures are used.
        Overall: O(1).

'''