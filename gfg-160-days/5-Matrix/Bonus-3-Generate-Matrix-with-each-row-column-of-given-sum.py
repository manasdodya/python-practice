'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-bonus-problem/problem/generate-a-matrix-with-each-row-and-column-of-given-sum

Given two integer arrays rowSum[] of size n and colSum[] of size m, the task is to construct a 2D matrix of size n x m such that the sum of matrix elements in ith row is rowSum[i] and the sum of matrix elements in jth column is colSum[j].
Note: Since multiple answers are possible, return any one of them. 
Arrays are generated such that answer is always possible.
The driver code will print true if output matrix is correct, otherwise it will print false.

Examples:

Input: rowSum[] = [5, 7, 10], colSum[] = [8, 6, 8]
Output: true
Explanation: For the matrix [[0, 5, 0], [6, 1, 0], [2, 0, 8]], we have row 1 with sum equal to 5 and column 1 has sum equal to 8.Row 2 has sum equal to 7 and column 2 has sum equal to 6.Row 3 has sum equal to 10 and column 3 has sum equal to 8.

Input: rowSum[] = [1, 0], colSum[] = [1]
Output: true
Explanation: For the matrix [[1], [0]], we have row 1 with sum equal to 1 and column 1 has sum equal to 1.Row 2 with sum equal to 0.

Constraints:
1 <= n, m <= 103
1 <= rowSum[i] <= 103
1 <= colSum[i] <= 103
'''
def constructMatrix(rowSum, colSum):
    n = len(rowSum)
    m = len(colSum)
    matrix = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            # Place the minimum of remaining rowSum and colSum
            value = min(rowSum[i], colSum[j])
            matrix[i][j] = value
            
            # Update rowSum and colSum
            rowSum[i] -= value
            colSum[j] -= value
    
    return matrix

# Example Usage
rowSum1 = [5, 7, 10]
colSum1 = [8, 6, 8]
matrix1 = constructMatrix(rowSum1[:], colSum1[:])
print("Matrix 1:", matrix1)  # Check validity manually or via driver code

rowSum2 = [1, 0]
colSum2 = [1]
matrix2 = constructMatrix(rowSum2[:], colSum2[:])
print("Matrix 2:", matrix2)  # Check validity manually or via driver code

'''
Approach:

    Initialize the Matrix:
        Create a n x m matrix initialized with zeros.

    Greedy Filling:
        Start from the first row and column. For each cell (i,j):
            Place the minimum of the remaining row sum (rowSum[i]) and column sum (colSum[j]) into the cell.
            Deduct the placed value from both rowSum[i] and colSum[j].
        Move to the next cell and repeat until all values in rowSum and colSum are zero.

    Output:
        Return the constructed matrix.

        
Example Outputs:
Input 1:

rowSum = [5, 7, 10], colSum = [8, 6, 8]

Output Matrix:

[[5, 0, 0], 
 [3, 4, 0], 
 [0, 2, 8]]

Input 2:

rowSum = [1, 0], colSum = [1]

Output Matrix:

[[1], 
 [0]]

Complexity:

    Time Complexity: O(n×m)O(n×m)
        We iterate over all cells of the matrix.

    Space Complexity: O(1)O(1)
        We use the given matrix and modify it in place, apart from negligible auxiliary variables.


'''