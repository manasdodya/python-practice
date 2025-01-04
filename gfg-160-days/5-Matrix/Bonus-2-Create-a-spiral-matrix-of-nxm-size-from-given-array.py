'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-bonus-problem/problem/create-a-spiral-matrix-of-nm-size-from-given-array

You are given two positive integers n and m, and an integer array arr[] containing total (n*m) elements. Return a 2D matrix of dimensions n x m by filling it in a clockwise spiral order using the elements from the given array.

Examples:

Input: n = 4, m = 4, arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Output: [[1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]]

Input: n = 3, m = 4, arr[] =[1, 8, 6, 3, 8, 6, 1, 6, 3, 2, 5, 3]
Output: [[1, 8, 6, 3],
        [2, 5, 3, 8],
        [3, 6, 1, 6]]

Input: n = 2, m = 2, arr[] =[1, 8, 6, 3]
Output: [[1, 8],
        [3, 6]]

Constraints:
1 ≤ n, m ≤ 103
arr.size() = n x m
1 ≤ arr[i] ≤ 103

'''
def fill_spiral_matrix(n, m, arr):
    # Initialize an empty n x m matrix
    matrix = [[0] * m for _ in range(n)]
    
    # Initialize bounds
    top, bottom, left, right = 0, n - 1, 0, m - 1
    index = 0  # To traverse through the array
    
    # Fill the matrix in a spiral order
    while index < len(arr):
        # Fill the top row
        for i in range(left, right + 1):
            if index < len(arr):
                matrix[top][i] = arr[index]
                index += 1
        top += 1
        
        # Fill the right column
        for i in range(top, bottom + 1):
            if index < len(arr):
                matrix[i][right] = arr[index]
                index += 1
        right -= 1
        
        # Fill the bottom row (if not already traversed)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                if index < len(arr):
                    matrix[bottom][i] = arr[index]
                    index += 1
            bottom -= 1
        
        # Fill the left column (if not already traversed)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if index < len(arr):
                    matrix[i][left] = arr[index]
                    index += 1
            left += 1
    
    return matrix

# Example usage
n1, m1, arr1 = 4, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
n2, m2, arr2 = 3, 4, [1, 8, 6, 3, 8, 6, 1, 6, 3, 2, 5, 3]
n3, m3, arr3 = 2, 2, [1, 8, 6, 3]

print(fill_spiral_matrix(n1, m1, arr1))
print(fill_spiral_matrix(n2, m2, arr2))
print(fill_spiral_matrix(n3, m3, arr3))


'''
To fill a 2D matrix in a clockwise spiral order using the elements of the given array, we need to iteratively populate the boundaries of the matrix while progressing inward. Here's how we can achieve this:
Plan:

    Initialize Variables:
        top, bottom, left, right to define the current bounds of the matrix.
        An index pointer to iterate through the array.

    Spiral Traversal:
        Fill the top row, move down the right column, fill the bottom row (if not already traversed), and finally move up the left column (if not already traversed).
        Shrink the bounds (top++, bottom--, left++, right--) after completing each boundary traversal.

    Stop Condition:
        Stop when all the elements of the array have been placed in the matrix.

    Edge Cases:
        Handle small matrices (e.g., 1×m1×m or n×1n×1) gracefully.

Output:

For the inputs provided:

Input 1:

n = 4, m = 4, arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

Output:

[[1, 2, 3, 4],
 [12, 13, 14, 5],
 [11, 16, 15, 6],
 [10, 9, 8, 7]]

Input 2:

n = 3, m = 4, arr = [1, 8, 6, 3, 8, 6, 1, 6, 3, 2, 5, 3]

Output:

[[1, 8, 6, 3],
 [2, 5, 3, 8],
 [3, 6, 1, 6]]

Input 3:

n = 2, m = 2, arr = [1, 8, 6, 3]

Output:

[[1, 8],
 [3, 6]]

Complexity:

    Time Complexity: O(n * m)O
        Each element is visited once.

    Space Complexity: O(1)
        In-place matrix filling without using extra space beyond variables.
'''