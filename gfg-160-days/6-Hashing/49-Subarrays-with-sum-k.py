'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/subarrays-with-sum-k

Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.

Examples:

Input: arr = [10, 2, -2, -20, 10], k = -10
Output: 3
Explaination: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.

Input: arr = [9, 4, 20, 3, 10, 5], k = 33
Output: 2
Explaination: Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.

Input: arr = [1, 3, 5], k = 0
Output: 0
Explaination: No subarray with 0 sum.

Constraints:

    1 ≤ arr.size() ≤ 105
    -103 ≤ arr[i] ≤ 103
    -107 ≤ k ≤ 107
'''

def subarraySum(arr, k):
    # Initialize a hashmap (dictionary) to store the frequency of prefix sums
    prefix_sum_count = {0: 1}  # We need to consider subarrays starting from index 0
    current_prefix_sum = 0
    count = 0
    
    # Traverse the array
    for num in arr:
        current_prefix_sum += num
        
        # If (current_prefix_sum - k) exists in the hashmap, increment count by its frequency
        if current_prefix_sum - k in prefix_sum_count:
            count += prefix_sum_count[current_prefix_sum - k]
        
        # Update the frequency of the current prefix sum in the hashmap
        if current_prefix_sum in prefix_sum_count:
            prefix_sum_count[current_prefix_sum] += 1
        else:
            prefix_sum_count[current_prefix_sum] = 1
    
    return count

# Test cases
print(subarraySum([10, 2, -2, -20, 10], -10))  # Output: 3
print(subarraySum([9, 4, 20, 3, 10, 5], 33))  # Output: 2
print(subarraySum([1, 3, 5], 0))  # Output: 0

'''
Algorithm Explanation

    Prefix Sum:
        The prefix sum up to index i is the sum of all elements from the beginning of the array to index i.
        If prefix_sum[i] is the sum from the start to index i, then for any subarray arr[l...r], 
        the sum of that subarray is: \text{sum}(arr[l...r]) = \text{prefix_sum}[r] - \text{prefix_sum}[l-1]
        If this sum is equal to k, we can say that the sum of the subarray from l to r equals k.

    Hashmap (or Dictionary):
        Use a hashmap to store how many times each prefix sum occurs while iterating over the array.
        At each index i, calculate the current prefix sum. If current_prefix_sum - k has been encountered before, 
        it means there exists a subarray ending at index i that has a sum equal to k.

    Steps:
        Initialize current_prefix_sum = 0 and a hashmap to store the frequency of prefix sums. 
        Initially, store {0: 1} to account for the case where a subarray sum equals k starting from the beginning.
        Traverse the array and update current_prefix_sum.
        If current_prefix_sum - k is present in the hashmap, it means there exists a subarray that has sum k. 
        The number of times current_prefix_sum - k appeared will tell us how many subarrays end at the current index with sum equal to k.
        Update the hashmap with the current prefix sum.

Time Complexity:

    The time complexity is O(n) because we are iterating over the array once and each operation (hashmap lookup and insertion) takes O(1) time on average.

Space Complexity:

    The space complexity is O(n) because in the worst case, all prefix sums are unique, and we store them in the hashmap.

Explanation of Code:

    prefix_sum_count = {0: 1}:
        This is initialized to store the frequency of prefix sums, with {0: 1} to account for the edge case where the subarray starts from the beginning of the array and directly sums to k.

    current_prefix_sum += num:
        We accumulate the sum of elements as we traverse the array. This represents the prefix sum up to the current index.

    if current_prefix_sum - k in prefix_sum_count:
        This checks if there exists a previous prefix sum such that the difference between the current prefix sum and k gives us a valid subarray with sum k. If it exists, it means there are one or more subarrays ending at the current index that sum to k, and we increment the count by the frequency of current_prefix_sum - k.

    prefix_sum_count[current_prefix_sum] += 1:
        After processing the current element, we update the frequency of the current prefix sum in the hashmap.

Example Walkthrough:

For the input array arr = [10, 2, -2, -20, 10] and k = -10:

    Initially, prefix_sum_count = {0: 1}, current_prefix_sum = 0, count = 0.

    First element (10):
        current_prefix_sum = 10
        No match (10 - (-10) = -20 not in hashmap).
        Update hashmap: prefix_sum_count = {0: 1, 10: 1}.

    Second element (2):
        current_prefix_sum = 12
        No match (12 - (-10) = -22 not in hashmap).
        Update hashmap: prefix_sum_count = {0: 1, 10: 1, 12: 1}.

    Third element (-2):
        current_prefix_sum = 10
        Match (10 - (-10) = -20 is in hashmap, 1 occurrence).
        Increment count: count = 1.
        Update hashmap: prefix_sum_count = {0: 1, 10: 2, 12: 1}.

    Fourth element (-20):
        current_prefix_sum = -10
        Match (-10 - (-10) = -20 is in hashmap, 1 occurrence).
        Increment count: count = 2.
        Update hashmap: prefix_sum_count = {0: 1, 10: 2, 12: 1, -10: 1}.

    Fifth element (10):
        current_prefix_sum = 0
        Match (0 - (-10) = -10 is in hashmap, 1 occurrence).
        Increment count: count = 3.
        Update hashmap: prefix_sum_count = {0: 2, 10: 2, 12: 1, -10: 1}.

Final count is 3, which is the correct answer.

'''