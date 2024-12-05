'''
URL - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751

Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
'''

def push_zeros_to_end(arr):
    n = len(arr)
    j = 0  # Pointer for the position of the next non-zero element

    for i in range(n):
        if arr[i] != 0:
            # Swap non-zero element at i with the element at j
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

# Example usage
print(push_zeros_to_end([1, 2, 0, 4, 3, 0, 5, 0]))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]
print(push_zeros_to_end([10, 20, 30]))             # Output: [10, 20, 30]
print(push_zeros_to_end([0, 0]))                   # Output: [0, 0]


'''
Algorithm:

    Initialize a Pointer:
        Use a pointer j to track the position where the next non-zero element should be placed.

    Traverse the Array:
        Iterate through the array with an index i.
        If the current element is non-zero, swap it with the element at index j and increment j.

    Result:
        By the end of the traversal, all non-zero elements will be moved to the front, and all zeros will naturally be at the end.

Explanation:

    Input: [1, 2, 0, 4, 3, 0, 5, 0]
        During the traversal:
            i=0: arr[0] is non-zero, swap with arr[0] (no change), j=1.
            i=1: arr[1] is non-zero, swap with arr[1] (no change), j=2.
            i=2: arr[2] is zero, do nothing.
            i=3: arr[3] is non-zero, swap with arr[2], arr=[1, 2, 4, 0, 3, 0, 5, 0], j=3.
            Continue similarly for other indices.
        Result: [1, 2, 4, 3, 5, 0, 0, 0].

    Input: [10, 20, 30]
        All elements are non-zero, so no swaps are performed.
        Result: [10, 20, 30].

    Input: [0, 0]
        All elements are zero, so no swaps are performed.
        Result: [0, 0].

Complexity:

    Time Complexity: O(n), as the array is traversed once.
    Space Complexity: O(1), as no extra space is used apart from a few variables.

Key Properties:

    The method is in-place, making it efficient for large arrays.
    The order of non-zero elements is preserved.

'''