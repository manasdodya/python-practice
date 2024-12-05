'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/smallest-positive-missing-number-1587115621

Problem-Statement:
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
Note: Positive number starts from 1. The array can have negative integers too.

Examples:

Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.

Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.

Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1.

Constraints:
1 <= arr.size() <= 105
-106 <= arr[i] <= 106
'''


def smallest_missing_positive(arr):
    n = len(arr)
    
    # Step 1: Replace out-of-range numbers with a dummy value (n+1)
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = n + 1
    
    # Step 2: Use index marking
    for i in range(n):
        num = abs(arr[i])
        if 1 <= num <= n:
            arr[num - 1] = -abs(arr[num - 1])
    
    # Step 3: Find the first missing positive number
    for i in range(n):
        if arr[i] > 0:
            return i + 1
    
    # If all numbers from 1 to n are present
    return n + 1

# Example usage
print(smallest_missing_positive([2, -3, 4, 1, 1, 7]))  # Output: 3
print(smallest_missing_positive([5, 3, 2, 5, 1]))      # Output: 4
print(smallest_missing_positive([-8, 0, -1, -4, -3]))  # Output: 1

'''
Algorithm Steps:

    Replace Irrelevant Numbers:
        Replace all numbers less than 1 or greater than nn with a dummy number (e.g., n+1n+1). This step ensures that we only focus on numbers in the range [1,n][1,n].

    Mark Numbers Using Indices:
        For every valid number xx in the range [1,n][1,n], mark its corresponding index x-1 in the array as negative. This indicates that the number xx exists.

    Find the First Missing Positive:
        Traverse the array. The first positive value at index ii indicates that i+1i+1 is the missing positive number.

    Edge Case:
        If all indices are marked, return n+1n+1.

Explanation of Examples:
Example 1:

Input: [2,-3,4,1,1,7][2,-3,4,1,1,7]

    Replace irrelevant numbers: [2,7,4,1,1,7][2,7,4,1,1,7]
    Mark indices: [2,-7,-4,-1,1,7][2,-7,-4,-1,1,7]
    Traverse to find the first positive number: Index 2 corresponds to 33.

Example 2:

Input: [5,3,2,5,1][5,3,2,5,1]

    Replace irrelevant numbers: [5,3,2,5,1][5,3,2,5,1]
    Mark indices: [-5,-3,-2,5,-1][-5,-3,-2,5,-1]
    Traverse to find the first positive number: Index 3 corresponds to 44.

Example 3:

Input: [-8,0,-1,-4,-3][-8,0,-1,-4,-3]

    Replace irrelevant numbers: [6,6,6,6,6][6,6,6,6,6] (All numbers irrelevant)
    Mark indices: Unchanged as no valid numbers.
    Traverse to find the first positive number: 11.

Complexity:

    Time Complexity: O(n)O(n) because we traverse the array a constant number of times.
    Space Complexity: O(1)O(1), as we only modify the array in place.

'''