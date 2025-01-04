'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-bonus-problem/problem/c-matrix-rotation-by-180-degree0745

Given a 2D square matrix mat[][] of size n x n, turn it by 180 degrees without using extra space.

Note: You must rotate the matrix in place and modify the input matrix directly.

Examples:

Input: mat[][] = [[1, 2],
                [3, 4]]
Output: [[4, 3], 
        [2, 1]]

Input:  mat[][] = [[1, 2, 3, 4], 
                 [5, 6, 7 ,8], 
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]
Output: [[16, 15, 14, 13], 
        [12, 11, 10, 9], 
        [8, 7, 6, 5], 
        [4, 3, 2, 1]]

Constraints:
1 ≤ n ≤ 500
0 <= mat[i][j] <= 104

'''
def rotate_matrix_180(mat):
    n = len(mat)
    
    # Traverse half the rows
    for i in range((n + 1) // 2):  # Includes middle row for odd-sized matrices
        for j in range(n):  # Traverse all columns
            # Calculate the corresponding position for swapping
            x, y = n - 1 - i, n - 1 - j
            # Avoid double swapping in the middle row of odd-sized matrices
            if (i == x and j > y):
                break
            # Swap elements
            mat[i][j], mat[x][y] = mat[x][y], mat[i][j]
    
    return mat

# Example usage
mat1 = [[1, 2], 
        [3, 4]]

mat2 = [[1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

print(rotate_matrix_180(mat1))  # Output: [[4, 3], [2, 1]]
print(rotate_matrix_180(mat2))  # Output: [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]


'''
Plan:

    Symmetric Swapping:
        Each element in the top-left portion of the matrix is swapped with its corresponding element in the bottom-right portion.
        Similarly, the elements in the bottom-left are swapped with the top-right.

    Swap Logic:
        For a cell mat[i][j], its corresponding position after a 180-degree rotation is mat[n−1−i][n−1−j].

    Single Pass:
        Traverse only half the matrix (both row-wise and column-wise) to perform the swaps, avoiding double-swapping elements.

    Special Cases:
        Handle the center element separately for odd-sized matrices. No action is needed for even-sized matrices.

Explanation:

    Outer Loop:
        Iterates over rows from the top up to the middle of the matrix.
        The condition (n + 1) // 2 ensures we cover all rows for even-sized matrices and includes the middle row for odd-sized matrices.

    Inner Loop:
        Iterates over all columns in the current row. Handles swapping with the corresponding cell at the bottom-right of the matrix.

    Avoid Overlapping Swaps:
        For odd-sized matrices, in the middle row, avoid swapping elements beyond the midpoint by checking indices j>yj>y.

    In-Place Modification:
        No extra memory is used. The swaps are done directly on the input matrix.

Complexity:

    Time Complexity: O(n^2)
        Each element of the matrix is visited once for swapping.

    Space Complexity: O(1)
        No extra space is used apart from a few variables.

'''