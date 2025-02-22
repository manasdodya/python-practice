'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-bonus-problem/problem/longest-subarray-with-sum-divisible-by-k1259

Given an array arr[] and a positive integer k, find the length of the longest subarray with the sum of the elements divisible by k.
Note: If there is no subarray with sum divisible by k, then return 0.

Examples :

Input: arr[] = [2, 7, 6, 1, 4, 5], k = 3
Output: 4
Explanation: The subarray [7, 6, 1, 4] has sum = 18, which is divisible by 3.

Input: arr[] = [-2, 2, -5, 12, -11, -1, 7], k = 3
Output: 5
Explanation: The subarray [2, -5, 12, -11, -1] has sum = -3, which is divisible by 3.

Input: arr[] = [1, 2, -2], k = 2
Output: 2
Explanation: The subarray is [2, -2] has sum = 0, which is divisible by 2.

Constraints:
1 <= arr.size() <= 106
1 <= k <= 106
-106 <= arr[i] <= 106
'''

def longestSubarrayDivByK(arr, k):
    remainder_index = {0: -1}  # To handle cases where prefix sum itself is divisible by k
    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(arr):
        prefix_sum += num
        rem = prefix_sum % k  # Compute remainder
        
        # Ensure remainder is non-negative
        if rem < 0:
            rem += k  

        # If remainder was seen before, update max_length
        if rem in remainder_index:
            max_length = max(max_length, i - remainder_index[rem])
        else:
            remainder_index[rem] = i  # Store first occurrence of remainder

    return max_length

# Example Test Cases
arr1, k1 = [2, 7, 6, 1, 4, 5], 3
arr2, k2 = [-2, 2, -5, 12, -11, -1, 7], 3
arr3, k3 = [1, 2, -2], 2

print(longestSubarrayDivByK(arr1, k1))  # Output: 4
print(longestSubarrayDivByK(arr2, k2))  # Output: 5
print(longestSubarrayDivByK(arr3, k3))  # Output: 2

'''
Key Observations

    Using Prefix Sum Modulo k:
        Let prefix_sum[i] be the sum of elements from index 0 to i.
        If prefix_sum[j] % k == prefix_sum[i] % k for any j < i, then the sum of subarray arr[j+1:i] is divisible by kk.
        This means we can track first occurrences of remainder values in a hashmap.

    Using a Hash Map (remainder_index):
        Store the first occurrence index of each remainder when taking prefix_sum % k.
        Whenever the same remainder appears again, check the length of the subarray and update the maximum length.

    Handling Negative Remainders:
        Since modulo operation in Python can yield negative values, adjust it using:

rem = (rem + k) % k

This ensures all remainders are positive.

Example Walkthrough
Example 1

Input:

arr = [2, 7, 6, 1, 4, 5], k = 3

Computation:

    Compute prefix sum and mod k:

    Prefix Sum: 2 → 9 → 15 → 16 → 20 → 25
    Modulo k :  2 → 0 → 0  → 1  → 2  → 1

    The longest subarray where the remainder repeats is [7, 6, 1, 4] (length = 4).
    Output: 4.

Example 2

Input:

arr = [-2, 2, -5, 12, -11, -1, 7], k = 3

    Compute prefix sum:

    Prefix Sum: -2 → 0 → -5 → 7 → -4 → -5 → 2
    Modulo k :  1  → 0 → 1  → 1 → 2  → 1  → 2

    Longest subarray found: [2, -5, 12, -11, -1] (length = 5).
    Output: 5.

Complexity Analysis

    Time Complexity: O(N), since we iterate through arr[] once.
    Space Complexity: O(K), for storing remainder indices.
'''