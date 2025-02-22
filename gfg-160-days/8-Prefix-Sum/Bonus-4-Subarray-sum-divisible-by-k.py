'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-bonus-problem/problem/sub-array-sum-divisible-by-k2617

You are given an integer array arr[] and a value k. The task is to find the count of all sub-arrays whose sum is divisible by k.

Examples:

Input: arr[] = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
Explanation: There are 7 sub-arrays whose sum is divisible by k: [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3] and [-2, -3]

Input: arr[] = [2, 2, 2, 2, 2, 2], k = 2
Output: 21
Explanation: All subarray sums are divisible by 2

Input: arr[] = [-1, -3, 2], k = 5
Output: 0
Explanation: There is no such sub-array whose sum is divisible by k.

Constraints:
1 ≤ arr.size() ≤ 104
-106 ≤ arr[i]≤ 106
1 ≤ k ≤ 104

'''
from collections import defaultdict

def subarraysDivByK(arr, k):
    remainder_count = defaultdict(int)
    remainder_count[0] = 1  # Initial case: prefix sum = 0 is always counted
    
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num
        rem = prefix_sum % k  # Compute remainder
        
        # Adjust for negative remainder
        if rem < 0:
            rem += k  

        # If rem was seen before, add the frequency to the count
        count += remainder_count[rem]

        # Update frequency of the remainder
        remainder_count[rem] += 1

    return count

# Example Test Cases
arr1, k1 = [4, 5, 0, -2, -3, 1], 5
arr2, k2 = [2, 2, 2, 2, 2, 2], 2
arr3, k3 = [-1, -3, 2], 5

print(subarraysDivByK(arr1, k1))  # Output: 7
print(subarraysDivByK(arr2, k2))  # Output: 21
print(subarraysDivByK(arr3, k3))  # Output: 0


'''
Algorithm Explanation

The problem requires counting subarrays whose sum is divisible by k. A brute force approach that iterates over all subarrays would take O(N2)O(N2) time, which is inefficient for large NN. Instead, we use the prefix sum + hash map technique for an optimized O(N)O(N) solution.
Efficient Approach (Prefix Sum + Hashing)

    Compute Prefix Sum Modulo k:
        If two prefix sums have the same remainder when divided by k, their difference is divisible by k.
        Example: If prefix sums at indices j and i have the same remainder, then the subarray arr[i+1:j] has a sum divisible by kk.

    Use a Hash Map (remainder_count):
        Store the frequency of each remainder value.
        For each prefix sum remainder rem, the number of subarrays ending at that index with sum divisible by kk is remainder_count[rem].

    Handle Negative Remainders:
        Since Python gives negative remainders for negative numbers, adjust as rem = (rem + k) % k to ensure a positive remainder.


Example Walkthrough
Example 1

Input:

arr = [4, 5, 0, -2, -3, 1], k = 5

Computation:

    Compute prefix sums and mod k:

    Prefix Sum: 4 → 9 → 9 → 7 → 4 → 5
    Modulo k :  4 → 4 → 4 → 2 → 4 → 0

    The remainder 4 appears multiple times, indicating valid subarrays.
    Result: 7 subarrays.

Example 2

Input:

arr = [2, 2, 2, 2, 2, 2], k = 2

    Since every number is divisible by k=2, every subarray will be counted.
    Result: 21 subarrays.

Example 3

Input:

arr = [-1, -3, 2], k = 5

    No valid subarrays found.
    Result: 0.

Complexity Analysis

    Time Complexity: O(N), as we iterate through arr[] once.
    Space Complexity: O(K), as we store at most k remainder values in a dictionary.
        
'''