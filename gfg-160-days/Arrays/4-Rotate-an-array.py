'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621

Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.

Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.

Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.

Constraints:
1 <= arr.size(), d <= 105
0 <= arr[i] <= 105
'''

def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # Adjust d for larger values
    
    # Helper function to reverse a subarray
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse the first d elements
    reverse(0, d - 1)
    
    # Step 2: Reverse the remaining elements
    reverse(d, n - 1)
    
    # Step 3: Reverse the entire array
    reverse(0, n - 1)
    
    return arr

# Example usage
arr1 = [1, 2, 3, 4, 5]
d1 = 2
print(rotate_array(arr1, d1))  # Output: [3, 4, 5, 1, 2]

arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d2 = 3
print(rotate_array(arr2, d2))  # Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]

arr3 = [7, 3, 9, 1]
d3 = 9
print(rotate_array(arr3, d3))  # Output: [3, 9, 1, 7]

'''
Approach: Reversal Algorithm

    Adjust dd: If dd is larger than the size of the array nn, use d=d%nd=d%n to handle the circular nature of the array.
    Reverse the First dd Elements: Reverse the subarray from index 0 to d-1d-1.
    Reverse the Remaining Elements: Reverse the subarray from index dd to n-1n-1.
    Reverse the Entire Array: Reverse the entire array to complete the left rotation.

Algorithm Steps:

    Reverse the first dd elements: [1,2,3,4,5]→[2,1,3,4,5][1,2,3,4,5]→[2,1,3,4,5]
    Reverse the remaining elements: [2,1,3,4,5]→[2,1,5,4,3][2,1,3,4,5]→[2,1,5,4,3]
    Reverse the entire array: [2,1,5,4,3]→[3,4,5,1,2][2,1,5,4,3]→[3,4,5,1,2]

Example 1:

Input:
arr = [1, 2, 3, 4, 5]
d = 2

Step-by-Step Explanation:

    Initial State:
    Array: [1, 2, 3, 4, 5], d=2d=2.

    Reverse the first d=2d=2 elements:
    Reverse subarray [1, 2]:
    Result: [2, 1, 3, 4, 5].

    Reverse the remaining n-d=3n-d=3 elements:
    Reverse subarray [3, 4, 5]:
    Result: [2, 1, 5, 4, 3].

    Reverse the entire array:
    Reverse the full array [2, 1, 5, 4, 3]:
    Result: [3, 4, 5, 1, 2].

Final Output: [3, 4, 5, 1, 2]

Example 2:

Input:
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d = 3

Step-by-Step Explanation:

    Initial State:
    Array: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d=3d=3.

    Reverse the first d=3d=3 elements:
    Reverse subarray [2, 4, 6]:
    Result: [6, 4, 2, 8, 10, 12, 14, 16, 18, 20].

    Reverse the remaining n-d=7n-d=7 elements:
    Reverse subarray [8, 10, 12, 14, 16, 18, 20]:
    Result: [6, 4, 2, 20, 18, 16, 14, 12, 10, 8].

    Reverse the entire array:
    Reverse the full array [6, 4, 2, 20, 18, 16, 14, 12, 10, 8]:
    Result: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6].

Final Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Example 3:

Input:
arr = [7, 3, 9, 1]
d = 9

Step-by-Step Explanation:

    Adjust dd:
    d=d%n=9%4=1d=d%n=9%4=1.

    Initial State:
    Array: [7, 3, 9, 1], d=1d=1.

    Reverse the first d=1d=1 element:
    Reverse subarray [7] (no change):
    Result: [7, 3, 9, 1].

    Reverse the remaining n-d=3n-d=3 elements:
    Reverse subarray [3, 9, 1]:
    Result: [7, 1, 9, 3].

    Reverse the entire array:
    Reverse the full array [7, 1, 9, 3]:
    Result: [3, 9, 1, 7].

Final Output: [3, 9, 1, 7]

Complexity Analysis

    Time Complexity: O(n): Each reversal involves traversing a part of the array, and we perform 3 reversals.
    Space Complexity: O(1): No additional space is used, and the array is modified in-place.
'''