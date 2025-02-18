'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-bonus-problems/problem/minimum-removals-for-target-sum

You are given an array of positive integers arr[] and an integer k. In one operation, you can remove either the leftmost or the rightmost element from the array. After each operation, the size of arr[] will be reduced by one.

Your task is to determine the minimum number of operations required to make the total sum of removed elements exactly equal to k. If it is not possible to achieve this, return -1.

Examples:

Input: arr[] = [3, 4, 1, 3, 2], k = 5
Output: 2
Explanation: Removing 3 from left and 2 from right gives a sum of 5 in 2 operations.

Input: arr[] = [5, 3, 4, 6, 2], k = 6
Output: -1
Explanation: It is impossible to achieve the sum of removed elements as 6.

Input: arr[] = [1, 1, 3, 1, 2], k = 4
Output: 3
Explanation: Removing 1, 1 from left and 2 from right gives a sum of 4 in 3 operation.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
1 ≤ k ≤ arr.size()
'''

def min_operations(arr, k):
    total_sum = sum(arr)
    target = total_sum - k
    if target < 0:  
        return -1  # Impossible to remove elements and get sum k
    
    if target == 0:  
        return len(arr)  # Removing all elements gives sum k
    
    left, current_sum = 0, 0
    max_subarray_length = -1  # To store the longest subarray with sum = target

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1
        
        if current_sum == target:
            max_subarray_length = max(max_subarray_length, right - left + 1)
    
    return len(arr) - max_subarray_length if max_subarray_length != -1 else -1

# Test Cases
print(min_operations([3, 4, 1, 3, 2], 5))  # Output: 2
print(min_operations([5, 3, 4, 6, 2], 6))  # Output: -1
print(min_operations([1, 1, 3, 1, 2], 4))  # Output: 3
print(min_operations([2, 3, 1, 1, 2, 3], 7))  # Output: 3
print(min_operations([1, 2, 3, 4, 5], 15))  # Output: 5

'''
This problem can be solved efficiently using a Sliding Window + Two Pointer approach.
Key Observations

    We need to remove elements from either the leftmost (arr[0]) or the rightmost (arr[n-1]) side.
    Instead of explicitly removing elements, we can find a contiguous subarray that sums up to sum(arr) - k.
    The minimum operations required will then be:
    min_operations = n -  max subarray length with sum (sum(arr) - k)
    

Why this works?

    Instead of focusing on the removed elements, we focus on the remaining subarray.
    If we can find a longest contiguous subarray with sum sum(arr) - k, the remaining operations will be the number of elements removed.

    
Example Walkthrough
Example 1

Input: arr = [3, 4, 1, 3, 2], k = 5
Total sum: 3 + 4 + 1 + 3 + 2 = 13
Target sum of remaining elements: 13 - 5 = 8

Finding the longest subarray with sum = 8:

    Subarray [4, 1, 3] has sum 8 (length 3).
    We remove n - length = 5 - 3 = 2 elements.

Output: 2
Complexity Analysis

    Sliding Window: O(N)
    Space Complexity: O(1)
'''