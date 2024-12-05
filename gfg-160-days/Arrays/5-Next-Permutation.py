'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/next-permutation5226

Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.

Input: arr = [3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation, the next permutation is the lowest one.

Input: arr = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]
Explanation: The next permutation of the given array is {3, 4, 5, 1, 2}.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
'''

def next_permutation(arr):
    n = len(arr)
    
    # Step 1: Find the first pair where arr[i] < arr[i + 1]
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    # Step 2: If no such pair exists, reverse the entire array (it's the last permutation)
    if i == -1:
        arr.reverse()
        return arr
    
    # Step 3: Find the largest index j such that arr[j] > arr[i]
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    
    # Step 4: Swap elements at i and j
    arr[i], arr[j] = arr[j], arr[i]
    
    # Step 5: Reverse the subarray from i + 1 to the end
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return arr

# Example usage
print(next_permutation([2, 4, 1, 7, 5, 0]))  # Output: [2, 4, 5, 0, 1, 7]
print(next_permutation([3, 2, 1]))            # Output: [1, 2, 3]
print(next_permutation([3, 4, 2, 5, 1]))     # Output: [3, 4, 5, 1, 2]

'''
To find the next lexicographical permutation of an array of integers, we need to rearrange the elements in a way that results in the smallest possible permutation that is greater than the current one. If no greater permutation exists (i.e., the array is in descending order), we return the smallest permutation (i.e., sorted in ascending order).
Steps to Solve:

    Find the rightmost ascent:
        Traverse the array from right to left, and find the first pair of elements where the previous element is smaller than the next. This element is the "pivot". This step ensures that we can increment the permutation in a lexicographical manner.

    Find the smallest element greater than the pivot:
        Once we have the pivot, traverse from the right end again and find the smallest element that is larger than the pivot. Swap these two elements.

    Reverse the part after the pivot:
        Since the elements after the pivot are in descending order, reversing this part will give us the smallest lexicographical order.

    Handle edge case:
        If no pivot is found (i.e., the entire array is in descending order), the next permutation is the smallest permutation, which is simply the sorted array.

Algorithm:

    Find the largest index i such that arr[i] < arr[i + 1]. This is the pivot.
    Find the largest index j greater than i such that arr[j] > arr[i].
    Swap elements at i and j.
    Reverse the subarray from i + 1 to the end to get the next lexicographical permutation.

        sible increment.

    Swap the pivot and the found element:
        Swap these two elements to increment the permutation.

    Reverse the suffix:
        Since the suffix is in descending order, reversing it ensures it is in the smallest lexicographical order.

Complexity:

    Time Complexity: O(n), where n is the size of the array. We perform a constant number of passes through the array.
    Space Complexity: O(1), as we are modifying the array in place without using extra space.

Example Walkthrough:

    Input: [2, 4, 1, 7, 5, 0]
        Step 1: Find the first pair where arr[i] < arr[i + 1]. This happens at i = 3 (i.e., 7 < 5 is false, but 1 < 7 is true).
        Step 2: Find j = 4 such that arr[j] > arr[i]. Swap them, resulting in [2, 4, 5, 7, 1, 0].
        Step 3: Reverse the suffix from i + 1 = 3 to the end: [2, 4, 5, 0, 1, 7].

    Input: [3, 2, 1]
        No element i where arr[i] < arr[i + 1] is found, so reverse the entire array: [1, 2, 3].

    Input: [3, 4, 2, 5, 1]
        Step 1: Find i = 2 where arr[i] < arr[i + 1] is true.
        Step 2: Find j = 3 such that arr[j] > arr[i]. Swap them: [3, 4, 5, 2, 1].
        Step 3: Reverse the suffix: [3, 4, 5, 1, 2].
'''