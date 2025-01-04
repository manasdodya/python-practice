'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-bonus-problem/problem/make-matrix-beautiful-1587115620

A beautiful matrix is a matrix in which the sum of elements in each row and column is equal. Given a square matrix mat[][]. Find the minimum number of operation(s) that are required to make the matrix beautiful. In one operation you can increment the value of any one cell by 1.

Examples:

Input: mat[][] = [[1, 2], [3, 4]]
Output: 4
Explanation: Increment value of cell(0, 0) by 3 and increment value of cell(0, 1) by 1. Hence total 4 operation are required. Such that all rows and columns have sum of 8.

Input: mat[][] = [[1, 2, 3], [4, 2, 3], [3, 2, 1]]
Output: 6
Explanation: Increment value of cell(0, 0) by 1, increment value of cell(0, 1) by 2, increment value of cell(2, 1) by 1, increment value of cell(2, 2) by 2. Such that all rows and columns have sum of 9.

Input: mat[][] = [[0, 2], [3, 4]]
Output: 5
Explanation: Increment value of cell(0, 0) by 4, increment value of cell(0, 1) by 1. Hence total 5 operation are required.

Constraints:
1 <= mat.size(), mat[0].size() <= 500
1 <= mat[i][j] <= 106
'''
def minOperationsToBeautifulMatrix(mat):
    n = len(mat)
    
    # Step 1: Calculate row sums and column sums
    rowSum = [sum(row) for row in mat]
    colSum = [sum(mat[i][j] for i in range(n)) for j in range(n)]
    
    # Step 2: Determine the target maxSum
    maxSum = max(max(rowSum), max(colSum))
    
    # Step 3: Calculate the minimum number of operations
    operations = 0
    for i in range(n):
        operations += maxSum - rowSum[i]
    
    return operations

# Example Usage
mat1 = [[1, 2], [3, 4]]
print(minOperationsToBeautifulMatrix(mat1))  # Output: 4

mat2 = [[1, 2, 3], [4, 2, 3], [3, 2, 1]]
print(minOperationsToBeautifulMatrix(mat2))  # Output: 6

mat3 = [[0, 2], [3, 4]]
print(minOperationsToBeautifulMatrix(mat3))  # Output: 5

'''
Observations:

    The target sum for each row and column in the matrix will be the maximum sum of any row or column in the original matrix. Let this be maxSummaxSum.
    To achieve a beautiful matrix, increment cells such that every row and every column sum equals maxSummaxSum.
    The total number of operations required is the sum of differences between maxSummaxSum and the current sum of each row.

Approach:

    Compute row and column sums:
        Calculate the sum of elements in each row and column.
        Determine maxSum=max(maximum row sum,maximum column sum).

    Increment cells to balance the matrix:
        For each row, calculate how much it needs to reach maxSummaxSum.
        Increment the cells to make up the difference.

    Output the total number of operations:
        Sum up all the increments made.

        
Example Walkthrough:
Input:

mat = [[1, 2],
       [3, 4]]

    Row sums: [3, 7]
    Column sums: [4, 6]
    maxSum: max(7,6)=7
    Operations:
        Row 1 needs 7−3=4 operations.
        Row 2 is already at 7, so no additional operations are needed.
        Total operations = 4.

Output: 4
Complexity:

    Time Complexity:
        Calculating row and column sums: O(n^2)
        Calculating operations: O(n)
        Overall: O(n^2)

    Space Complexity:
        Storage for row sums and column sums: O(n)
        Overall: O(n)
'''