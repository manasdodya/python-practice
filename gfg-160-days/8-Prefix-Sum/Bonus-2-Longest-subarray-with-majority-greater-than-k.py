'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-bonus-problem/problem/longest-subarray-with-majority-greater-than-k

Given an array arr[] and an integer k, the task is to find the length of longest subarray in which the count of elements greater than k is more than the count of elements less than or equal to k.

Examples:

Input: arr[] = [1, 2, 3, 4, 1] , k = 2
Output: 3
Explanation: The subarray [2, 3, 4] or [3, 4, 1] satisfy the given condition, and there is no subarray of length 4 or 5 which will hold the given condition, so the answer is 3.

Input: arr[] = [6, 5, 3, 4], k = 2
Output: 4
Explanation: In the subarray [6, 5, 3, 4], there are 4 elements > 2 and 0 elements <= 2, so it is the longest subarray.

Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 106
0 <= k <= 106
'''

def longest_subarray(arr, k):
    n = len(arr)
    transformed = [1 if num > k else -1 for num in arr]
    
    prefix_sum = 0
    prefix_map = {0: -1}  # Initialize with base case (handles edge cases)
    max_length = 0
    
    for i in range(n):
        prefix_sum += transformed[i]

        # If prefix sum is positive at any point, update max_length
        if prefix_sum > 0:
            max_length = i + 1
        
        # Store the first occurrence of a prefix sum
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
        
        # If prefix_sum - 1 exists, we found a subarray where sum > 0
        if prefix_sum - 1 in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum - 1])
    
    return max_length

# Example Test Cases
print(longest_subarray([1, 2, 3, 4, 1], 2))  # Output: 3
print(longest_subarray([6, 5, 3, 4], 2))  # Output: 4
print(longest_subarray([1, 1, 1, 1, 1], 2))  # Output: 0 (No elements > k)
print(longest_subarray([10, 20, 30, 40], 25))  # Output: 2

'''
Algorithm Explanation

The problem requires us to find the longest contiguous subarray where the count of elements greater than k is more than the count of elements less than or equal to k.
Approach

    Transform the Array:
        Convert the array elements into +1 if they are greater than k, else -1.
        The problem now reduces to finding the longest subarray with a positive sum.

    Finding the Longest Subarray with Positive Sum:
        Use the prefix sum and hash map technique to track the first occurrence of each prefix sum.
        If a prefix sum has been seen before, the difference can be used to find the longest valid subarray.

    Implementation Details:
        Convert elements into +1 or -1.
        Maintain a running prefix sum.
        Use a hash map to store the first occurrence of each prefix sum.
        Check for the longest subarray where sum remains positive.

        
Example Walkthrough
Example 1:

Input: arr = [1, 2, 3, 4, 1], k = 2
Transformed Array: [-1, -1, +1, +1, -1]

    Prefix sum traversal:

    -1, -2, -1, 0, -1

    Longest subarray with sum > 0: Length = 3 ([2, 3, 4])

Output: 3

Example 2:

Input: arr = [6, 5, 3, 4], k = 2
Transformed Array: [+1, +1, +1, +1]

    Since all elements are +1, the whole array is valid.

Output: 4
Complexity Analysis

    Time Complexity: O(N) → Single pass through array.
    Space Complexity: O(N) → Hash map for prefix sums.

'''