'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-row-wise-sorted-matrix

Given a row-wise sorted 2D matrix mat[][] of size n x m and an integer x, find whether element x is present in the matrix.
Note: In a row-wise sorted matrix, each row is sorted in itself, i.e. for any i, j within bounds, mat[i][j] <= mat[i][j+1].

Examples :

Input: mat[][] = [[3, 4, 9],[2, 5, 6],[9, 25, 27]], x = 9
Output: true
Explanation: 9 is present in the matrix, so the output is true.

Input: mat[][] = [[19, 22, 27, 38, 55, 67]], x = 56
Output: false
Explanation: 56 is not present in the matrix, so the output is false.

Input: mat[][] = [[1, 2, 9],[65, 69, 75]], x = 91
Output: false
Explanation: 91 is not present in the matrix.

Constraints:
1 <= n, m <= 1000
1 <= mat[i][j] <= 105
1 <= x <= 105
'''

def binary_search_row(row, x):
    """
    Perform binary search on a single row.
    Returns True if x is found, otherwise False.
    """
    left, right = 0, len(row) - 1
    while left <= right:
        mid = (left + right) // 2
        if row[mid] == x:
            return True
        elif row[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

def search_in_matrix(mat, n, m, x):
    """
    Search for x in a row-wise sorted matrix using binary search.
    """
    for row in mat:
        if binary_search_row(row, x):
            return True
    return False

# Input matrix
mat = [
    [3, 33, 72, 156, 175, 234, 313],
    [32, 96, 196, 199, 290, 348, 439],
    [23, 101, 155, 223, 261, 328, 417],
    [14, 88, 145, 193, 275, 311, 396],
    [13, 84, 115, 194, 253, 314, 327],
    [50, 83, 86, 141, 199, 254, 304],
    [32, 82, 168, 258, 285, 286, 321]
]
x = 86

# Size of the matrix
n, m = 7, 7

# Check if x is present
print(search_in_matrix(mat, n, m, x))  # Output: True

mat1 = [[3, 4, 9], [2, 5, 6], [9, 25, 27]]
x1 = 9
print(search_in_matrix(mat1, 3, 3, x1))  # Output: True

mat2 = [[19, 22, 27, 38, 55, 67]]
x2 = 56
print(search_in_matrix(mat2, 1, 6, x2))  # Output: False

mat3 = [[1, 2, 9], [65, 69, 75]]
x3 = 91
print(search_in_matrix(mat3, 2, 3, x3))  # Output: False

'''
Complexity:

    Time Complexity:
        Binary search for one row: O(logm).
        Iterating through all rows: O(n).
        Total: O(n⋅log m).

    Space Complexity:
        O(1), as no extra space is used.

'''