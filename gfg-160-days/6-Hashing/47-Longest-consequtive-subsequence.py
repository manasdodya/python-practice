'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/longest-consecutive-subsequence2449

Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:

Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.

Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 105
'''
def longestConsecutiveSubsequence(arr):
    # Convert the array into a set to remove duplicates and allow fast lookups
    num_set = set(arr)
    max_length = 0

    # Iterate through each element in the array
    for num in num_set:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            # Find the length of the consecutive sequence starting from 'num'
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            # Update the maximum length
            max_length = max(max_length, current_length)

    return max_length

# Test Cases
print(longestConsecutiveSubsequence([2, 6, 1, 9, 4, 5, 3]))  # Output: 6
print(longestConsecutiveSubsequence([1, 9, 3, 10, 4, 20, 2]))  # Output: 4
print(longestConsecutiveSubsequence([15, 13, 12, 14, 11, 10, 9]))  # Output: 7
print(longestConsecutiveSubsequence([]))  # Output: 0
print(longestConsecutiveSubsequence([100, 4, 200, 1, 3, 2]))  # Output: 4

'''
Approach:

    Store Elements in a Set:
        Use a set to store all elements of the array. This allows O(1)O(1) average time complexity for lookups.
    Iterate Through Each Element:
        For each element, check if it's the start of a sequence (i.e., element−1element−1 is not in the set).
        If it's the start of a sequence, iterate forward to find the length of the sequence.
    Track the Maximum Length:
        Update the maximum length whenever a longer sequence is found.

Time Complexity:

    O(n), where nn is the size of the array. Each element is processed once.
    Lookup and insertion in a set take O(1) on average.

Space Complexity:

    O(n) for the set.

'''