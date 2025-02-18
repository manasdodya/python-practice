'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-bonus-problems/problem/subarrays-with-at-most-k-distinct-integers

You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is at most k.

Note: A subarray is a contiguous part of an array.

Examples:

Input: arr[] = [1, 2, 2, 3], k = 2
Output: 9
Explanation: Subarrays with at most 2 distinct elements are: [1], [2], [2], [3], [1, 2], [2, 2], [2, 3], [1, 2, 2] and [2, 2, 3].

Input: arr[] = [1, 1, 1], k = 1
Output: 6
Explanation: Subarrays with at most 1 distinct element are: [1], [1], [1], [1, 1], [1, 1] and [1, 1, 1].

Input: arr[] = [1, 2, 1, 1, 3, 3, 4, 2, 1], k = 2
Output: 24
Explanation: There are 24 subarrays with at most 2 distinct elements.

Constraints:
1 ≤ arr.size() ≤ 104
1 ≤ k ≤ arr.size()
1≤ arri  ≤ arr.size()
'''

from collections import defaultdict

def count_subarrays_at_most_k(arr, k):
    if k == 0:
        return 0  # No subarrays possible if k = 0

    freq = defaultdict(int)  # Dictionary to store the frequency of elements
    left = 0
    count = 0
    distinct_count = 0

    for right in range(len(arr)):
        if freq[arr[right]] == 0:
            distinct_count += 1  # New distinct element
        freq[arr[right]] += 1

        while distinct_count > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                distinct_count -= 1  # Remove from distinct count
            left += 1  # Shrink the window

        count += (right - left + 1)  # Count valid subarrays

    return count

def count_subarrays_with_exactly_k(arr, k):
    return count_subarrays_at_most_k(arr, k)

# Example test cases
print(count_subarrays_with_exactly_k([1, 2, 2, 3], 2))  # Output: 9
print(count_subarrays_with_exactly_k([1, 1, 1], 1))     # Output: 6
print(count_subarrays_with_exactly_k([1, 2, 1, 1, 3, 3, 4, 2, 1], 2))  # Output: 24

'''
1. Algorithm Explanation

This problem requires us to count the number of subarrays where the number of distinct integers is at most k. A sliding window (two-pointer) approach is optimal for this problem.
Key Idea

The number of subarrays with at most k distinct elements can be calculated efficiently using the "at most k" trick:

    We count the number of subarrays with at most k distinct elements.
    We count the number of subarrays with at most k-1 distinct elements.
    The result is the difference between these two counts, giving the exact number of subarrays with exactly k distinct elements.

Steps

    Sliding Window Approach:
        Use two pointers, left and right, to define a window [left, right].
        Expand right to include new elements while maintaining at most k distinct elements.
        If the number of distinct elements exceeds k, move left forward to restore validity.
        Count the number of valid subarrays for every position of right.

Example 1

Input: arr = [1, 2, 2, 3], k = 2
Valid subarrays:
Window [left, right]	Subarrays Count
[1]	                         1
[1,2]	                     2
[1,2,2]                      3
[2]	                         1
[2,2]	                     2
[2,2,3]	                     3
[3]	                         1


Complexity Analysis

    Sliding window: O(N)
    Hash table operations: O(1) (average case)
    Total complexity: O(N) 
'''