'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/rotate-by-90-degree-1587115621

Given a square matrix mat[][] of size n x n. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space. 

Examples:

Input: mat[][] = [[1, 2, 3],
                [4, 5, 6]
                [7, 8, 9]]
Output: Rotated Matrix:
[3, 6, 9]
[2, 5, 8]
[1, 4, 7]

Input: mat[][] = [[1, 2],
                [3, 4]]
Output: Rotated Matrix:
[2, 4]
[1, 3]

Constraints:
1 ≤ n ≤ 102
0 <= mat[i][j] <= 103

'''

def rotate_matrix_anticlockwise(mat):
    n = len(mat)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # Step 2: Reverse each column
    for col in range(n):
        for row in range(n // 2):
            mat[row][col], mat[n - 1 - row][col] = mat[n - 1 - row][col], mat[row][col]
    
    return mat

# Example usage
examples = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2], [3, 4]],
]

for i, mat in enumerate(examples):
    print(f"Example {i+1}:")
    print("Original Matrix:")
    for row in mat:
        print(row)
    
    rotated = rotate_matrix_anticlockwise(mat)
    print("Rotated Matrix:")
    for row in rotated:
        print(row)
    print()

'''
To rotate a square matrix n x n  by 90 degrees anticlockwise in-place, we follow these steps:
Steps to Rotate the Matrix

    Transpose the Matrix:
        Convert all rows into columns. Swap mat[i][j] with mat[j][i] for i<j.

    Reverse Each Column:
        After transposing, reverse the order of elements in each column to achieve a 90-degree anticlockwise rotation.


Explanation of Examples
Input:

    mat=[[1,2,3],[4,5,6],[7,8,9]]

Steps:

    Transpose:
        mat=[[1,4,7],[2,5,8],[3,6,9]]

    Reverse Columns:
        Column 0: Reverse [1, 4, 7] → [3, 6, 9]
        Column 1: Reverse [2, 5, 8] → [2, 5, 8]
        Column 2: Reverse [3, 6, 9] → [1, 4, 7]

Output:

    mat=[[3,6,9],[2,5,8],[1,4,7]]mat=[[3,6,9],[2,5,8],[1,4,7]]

Complexity

    Time Complexity:
        Transposing: O(n^2) (iterate over half the matrix).
        Reversing Columns: O(n^2) (each column is reversed).

    Total: O(n^2).

    Space Complexity:
        O(1): No extra space is used beyond the matrix itself.
'''

