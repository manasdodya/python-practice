'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-bonus-problems/problem/subarrays-with-k-different-integers


You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is exactly k.

Note: A subarray is a contiguous part of an array.

Examples:

Input: arr[] = [1, 2, 2, 3], k = 2
Output: 4
Explanation: Subarrays formed with exactly 2 different integers are: arr[0..1], arr[0..2], arr[1..3] and arr[2..3].

Input: arr[] = [3, 1, 2, 2, 3], k = 3
Output: 4
Explanation: Subarrays formed with exactly 3 distinct integers are: arr[0..2], arr[0..3], arr[0..4], arr[1..4].

Input: arr[] = [1, 1, 1, 1], k = 2
Output: 0
Explanation: There is no subarray having exactly 2 distinct integers.

Constraints:
1 ≤ arr.size() ≤ 104
1 ≤ k ≤ arr.size()
1≤ arri  ≤ arr.size()

'''

from collections import defaultdict

def count_subarrays_at_most_k(arr, k):
    if k == 0:
        return 0  # No valid subarrays possible if k = 0

    freq = defaultdict(int)  # Dictionary to store frequency of elements
    left = 0
    count = 0
    distinct_count = 0

    for right in range(len(arr)):
        if freq[arr[right]] == 0:
            distinct_count += 1  # New distinct element
        freq[arr[right]] += 1

        while distinct_count > k:  # Reduce window size until distinct elements ≤ k
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                distinct_count -= 1  # Remove from distinct count
            left += 1

        count += (right - left + 1)  # Count valid subarrays ending at 'right'

    return count

def count_subarrays_exactly_k(arr, k):
    return count_subarrays_at_most_k(arr, k) - count_subarrays_at_most_k(arr, k - 1)

# Test Cases
print(count_subarrays_exactly_k([1, 2, 2, 3], 2))  # Output: 4
print(count_subarrays_exactly_k([3, 1, 2, 2, 3], 3))  # Output: 4
print(count_subarrays_exactly_k([1, 1, 1, 1], 2))  # Output: 0
print(count_subarrays_exactly_k([1, 2, 1, 3, 4], 3))  # Output: 3


'''
Algorithm
    We can solve this problem using the Sliding Window (Two Pointers) technique.
    Key Idea

    The number of subarrays with exactly kk distinct integers can be calculated as:
    count_exactly_k = count_at_most_k - count_at_most_(k-1)
    
    Why?
        count_at_most_k: Counts subarrays with at most k distinct elements.
        count_at_most_k-1: Counts subarrays with at most k-1 distinct elements.
        Subtracting these two gives us the count of subarrays with exactly k distinct elements.

Example Walkthrough
Example 1

Input: arr = [1, 2, 2, 3], k = 2

    count_at_most_k(2) = 9
    count_at_most_k(1) = 5
    count_exactly_k(2) = 9 - 5 = 4

Example 2

Input: arr = [3, 1, 2, 2, 3], k = 3

    count_at_most_k(3) = 10
    count_at_most_k(2) = 6
    count_exactly_k(3) = 10 - 6 = 4

Complexity Analysis

    Sliding Window Approach: O(N)
    Hash Table Operations: O(1) (average case)
    Total Complexity: O(N)

'''