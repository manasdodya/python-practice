'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-gfg-160/problem/longest-sub-array-with-sum-k0809

Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].

Constraints:
1 ≤ arr.size() ≤ 105
-104 ≤ arr[i] ≤ 104
-109 ≤ k ≤ 109
'''

def longest_subarray_with_sum_k(arr, k):
    # Initialize a dictionary to store the first occurrence of a prefix sum
    prefix_sum_map = {}
    current_sum = 0
    max_length = 0
    
    # Traverse the array
    for i in range(len(arr)):
        current_sum += arr[i]
        
        # If current_sum equals k, the subarray from 0 to i has a sum of k
        if current_sum == k:
            max_length = i + 1
        
        # If current_sum - k is found in the map, it means a subarray sum of k exists
        if current_sum - k in prefix_sum_map:
            max_length = max(max_length, i - prefix_sum_map[current_sum - k])
        
        # Store the first occurrence of the current_sum in the map
        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i
    
    return max_length

# Test cases
print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, -10], 15))  # Output: 6
print(longest_subarray_with_sum_k([-5, 8, -14, 2, 4, 12], -5))  # Output: 5
print(longest_subarray_with_sum_k([10, -10, 20, 30], 5))  # Output: 0

'''
Approach:

    Prefix Sum: We maintain a running sum as we iterate through the array. The sum at each index gives us the total sum of elements from the beginning to the current index.
    Hash Map (Dictionary): We use a hash map to store the first occurrence of each prefix sum. 
    This allows us to quickly determine if there exists a previous prefix sum such that the difference between the current sum and the previous sum is equal to k.
    Key Observation: If at index i, the sum from index 0 to i is current_sum, and there exists a previous sum prefix_sum such that:
    current_sum - prefix_sum=k
    Then the subarray between the previous index and the current index has a sum equal to k.

Steps:

    Initialize current_sum = 0 and max_length = 0.
    Traverse through the array, updating the current_sum.
    If current_sum == k, then the subarray from the start to the current index has sum k, so update the max_length.
    If (current_sum - k) is found in the hash map, it means there is a subarray (ending at the current index) with a sum equal to k.
    Store the current_sum in the hash map if it hasn't been seen before.

xplanation of the Code:

    prefix_sum_map stores the first occurrence of each current_sum.
    current_sum is the cumulative sum from the start to the current index.
    If at any index, current_sum - k is found in the map, it means there exists a subarray whose sum is exactly k.
    max_length keeps track of the longest subarray with sum k.

Time Complexity:

    Time Complexity: O(N), where N is the number of elements in the array. 
    We iterate through the array once, and each operation with the hash map (insertion and lookup) takes constant time on average.
    Space Complexity: O(N) due to the storage of the prefix sums in the hash map.

Edge Cases:

    Subarray from the start: If the subarray from index 0 to some index i has the sum k, it's handled by checking current_sum == k.
    No such subarray: If no subarray has the sum k, the function will return 0.

Test Results:

For the given test cases:

    Input: [10, 5, 2, 7, 1, -10], k = 15
        Output: 6 (correct)
    Input: [-5, 8, -14, 2, 4, 12], k = -5
        Output: 5 (correct)
    Input: [10, -10, 20, 30], k = 5
        Output: 0 (correct)

This approach should efficiently solve the problem for large arrays within the provided constraints.

'''