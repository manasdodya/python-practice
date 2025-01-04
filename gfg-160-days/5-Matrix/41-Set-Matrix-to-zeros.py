'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/set-matrix-zeroes

You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0 and do it in constant space complexity.

Examples:

Input: mat[][] = [[1, -1, 1],
                [-1, 0, 1],
                [1, -1, 1]]
Output: [[1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]]
Explanation: mat[1][1] = 0, so all elements in row 1 and column 1 are updated to zeroes.

Input: mat[][] = [[0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]]
Output: [[0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]]
Explanation: mat[0][0] and mat[0][3] are 0s, so all elements in row 0, column 0 and column 3 are updated to zeroes.

Constraints:
1 ≤ n, m ≤ 500
- 231 ≤ mat[i][j] ≤ 231 - 1
'''

def set_matrix_zeroes(mat):
    n, m = len(mat), len(mat[0])
    
    # Flags to check if first row or column needs to be zeroed
    first_row_zero = any(mat[0][j] == 0 for j in range(m))
    first_col_zero = any(mat[i][0] == 0 for i in range(n))
    
    # Mark zeros in first row and column
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
    
    # Update the rest of the matrix based on the markers
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
    
    # Zero out the first row if needed
    if first_row_zero:
        for j in range(m):
            mat[0][j] = 0
    
    # Zero out the first column if needed
    if first_col_zero:
        for i in range(n):
            mat[i][0] = 0
    
    return mat

# Example usage
mat1 = [[1, -1, 1],
        [-1, 0, 1],
        [1, -1, 1]]

mat2 = [[0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]]

print(set_matrix_zeroes(mat1))  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(set_matrix_zeroes(mat2))  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


'''
Algorithm:

    Mark Rows and Columns:
        Use the first row and the first column to store markers. If mat[i][j]mat[i][j] is 00, set mat[i][0]=0mat[i][0]=0 and mat[0][j]=0mat[0][j]=0.

    Handle First Row and Column Separately:
        Store a flag to determine whether the first row and/or the first column needs to be zeroed. This is because these will act as markers for the rest of the matrix.

    Update the Matrix:
        Traverse the matrix (excluding the first row and column). If any element in mat[i][0]mat[i][0] or mat[0][j]mat[0][j] is 00, set mat[i][j]mat[i][j] to 00.

    Zero Out First Row and Column:
        Use the flags to zero out the first row and column, if needed.

Explanation:

    Markers:
        The first row and column are used as markers. For example, if mat[i][j]=0mat[i][j]=0, we mark mat[i][0]=0mat[i][0]=0 and mat[0][j]=0mat[0][j]=0.

    Matrix Update:
        Using the markers, the rest of the matrix is updated in-place without extra space.

    Edge Cases:
        Handle cases where the first row or column contains a zero independently, as they act as markers.

Complexity:

    Time Complexity: O(n⋅m)
        You traverse the entire matrix twice: once to set markers and once to update the matrix.

    Space Complexity: O(1)
        No additional space is used beyond a few variables.

'''