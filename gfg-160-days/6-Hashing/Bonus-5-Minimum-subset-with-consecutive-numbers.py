'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-bonus-problem/problem/min-subsets-with-consecutive-numbers0601

Given an array of distinct positive numbers, the task is to calculate the minimum number of subsets (or subsequences) from the array such that each subset contains consecutive numbers.

Examples:

Input: arr[] = [100, 56, 5, 6, 102, 58, 101, 57, 7, 103]
Output:3
Explanation: {5, 6, 7}, {56, 57, 58}, {100, 101, 102, 103} are 3 subset in which numbers are consecutive.

Input: arr[] = [10, 100, 105]
Output: 3
Explanation: {10}, {100} and {105} are 3 subset in which numbers are consecutive. 

Expected Time Complexity: O(n*log(n))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 106
'''

def minSubsets(arr):
    # Use a set for efficient lookup
    num_set = set(arr)
    groups = 0

    # Iterate through the array to find starting points
    for num in arr:
        # Check if the current number is the start of a group
        if num - 1 not in num_set:
            # It's a start of a new group
            groups += 1
            # Traverse the consecutive sequence
            current = num
            while current + 1 in num_set:
                current += 1

    return groups

# Examples
print(minSubsets([100, 56, 5, 6, 102, 58, 101, 57, 7, 103]))  # Expected: 3
print(minSubsets([10, 100, 105]))  # Expected: 3


'''
Approach Using a Set

    Add Elements to a Set:
        Use a set to efficiently store and access elements of the array.
        A set allows O(1)O(1) average time complexity for lookups.

    Find the Start of Consecutive Groups:
        Iterate through the array, and for each element, check if it is the "start" of a consecutive group. An element is the start of a group if there is no element equal to element - 1 in the set.

    Count Groups:
        For each starting element, iterate through its consecutive sequence and count it as one group.

    Return the Count:
        The total number of starting points gives the number of consecutive groups.

Algorithm

    Create a Set:
        Store all elements in a set for efficient lookup.
    Identify Starting Points:
        A starting point is an element xx for which x−1x−1 is not in the set.
    Traverse Consecutive Numbers:
        From each starting point, count the length of the consecutive sequence.
    Count Groups:
        Increment the group count for each starting point.

        
Explanation of Examples

    Input: [100, 56, 5, 6, 102, 58, 101, 57, 7, 103]
        Set: {100, 56, 5, 6, 102, 58, 101, 57, 7, 103}
        Starting points:
            5 → Group: {5, 6, 7}
            56 → Group: {56, 57, 58}
            100 → Group: {100, 101, 102, 103}
        Output: 3.

    Input: [10, 100, 105]
        Set: {10, 100, 105}
        Starting points:
            10 → Group: {10}
            100 → Group: {100}
            105 → Group: {105}
        Output: 3.

Complexity Analysis

    Time Complexity:
        Set Construction: O(n).
        Iteration Over Array: O(n), as each element is processed once.
        Traversal of Consecutive Numbers: Each element is part of at most one traversal.
        Total: O(n).

    Space Complexity:
        The set requires O(n) space to store the array elements.
'''