'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-gfg-160/problem/largest-subarray-of-0s-and-1s

Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

Examples:

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.

Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.

Input: arr[] = [0]
Output: 0
Explnation: There is no subarray with an equal number of 0s and 1s.

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 1

'''
def longest_subarray_equal_zeros_ones(arr):
    prefix_map = {}  # HashMap to store first occurrence of prefix sums
    current_sum = 0
    max_length = 0
    
    for i in range(len(arr)):
        # Convert 0 to -1
        if arr[i] == 0:
            arr[i] = -1
        
        current_sum += arr[i]  # Running sum
        
        # If the sum is zero, the entire array from 0 to i has equal 0s and 1s
        if current_sum == 0:
            max_length = i + 1  # Update max length
        
        # If this sum has been seen before, a subarray with sum 0 exists
        if current_sum in prefix_map:
            max_length = max(max_length, i - prefix_map[current_sum])
        else:
            # Store the first occurrence of the sum
            prefix_map[current_sum] = i
    
    return max_length

# Test cases
print(longest_subarray_equal_zeros_ones([1, 0, 1, 1, 1, 0, 0]))  # Output: 6
print(longest_subarray_equal_zeros_ones([0, 0, 1, 1, 0]))        # Output: 4
print(longest_subarray_equal_zeros_ones([0]))                    # Output: 0


'''
Approach:

This problem can be transformed into the Longest Subarray with Sum = 0 by modifying the array:

    Convert all 0s to -1s, so that finding an equal number of 0s and 1s reduces to finding a subarray whose sum is 0.
    Use Prefix Sum + Hash Map to find the longest subarray with sum = 0 efficiently.

Steps:

    Modify the array: Convert 0 to -1.
    Prefix Sum with Hash Map:
        Maintain a running sum (current_sum).
        Store the first occurrence of each prefix sum in a hash map (prefix_map).
        If current_sum == 0, update the max length since a valid subarray is found from index 0 to i.
        If current_sum has been seen before in the hash map, update the max length.
        Otherwise, store the first occurrence of current_sum.

Explanation of the Code:

    Convert 0 to -1: This makes the problem a sum-finding problem.
    Maintain current_sum: Track the sum of elements as we iterate.
    Use a hash map (prefix_map):
        If current_sum repeats at index i, it means the subarray from prefix_map[current_sum] + 1 to i has a sum of 0, meaning it contains an equal number of 0s and 1s.
        We update max_length if we find a longer subarray.

Complexity Analysis:

    Time Complexity: O(N), since we traverse the array once.
    Space Complexity: O(N), since we use a hash map to store prefix sums.

'''