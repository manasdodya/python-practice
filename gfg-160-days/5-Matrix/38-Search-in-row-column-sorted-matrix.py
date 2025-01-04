'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-matrix17201720

Given a 2D integer matrix mat[][] of size n x m, where every row and column is sorted in increasing order and a number x, the task is to find whether element x is present in the matrix.

Examples:

Input: mat[][] = [[3, 30, 38],[20, 52, 54],[35, 60, 69]], x = 62
Output: false
Explanation: 62 is not present in the matrix, so output is false.

Input: mat[][] = [[18, 21, 27],[38, 55, 67]], x = 55
Output: true
Explanation: 55 is present in the matrix.

Input: mat[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]], x = 3
Output: true
Explanation: 3 is present in the matrix.

Constraints:
1 <= n, m <=1000
1 <= mat[i][j] <= 109
1<= x <= 109
'''
def matSearch(mat,k):

    n = len(mat)
    m = len(mat[0])
    i = 0
    j = m - 1

    while i < n and j >= 0:
        if k > mat[i][j]:
            i += 1
        elif k < mat[i][j]:
            j -= 1
        else:
            return True
    return False


print(matSearch([[3, 30, 38],[20, 52, 54],[35, 60, 69]], 62))
print(matSearch([[18, 21, 27],[38, 55, 67]],55))
print(matSearch([[1, 2, 3],[4, 5, 6],[7, 8, 9]],3))


'''
Algorithm (Optimized O(n + m)):

    Start from the top-right corner of the matrix:
        Position: (i,j), where i=0 and j=m−1 (first row, last column).
    Compare the current element mat[i][j] with x:
        If mat[i][j]==x , return true.
        If mat[i][j]>x, move left (j=j−1).
        If mat[i][j]<x, move down (i=i+1).
    Repeat until:
        ii exceeds the number of rows (i≥n) or jj becomes negative (j<0).
    If no match is found, return false.


Explanation of Examples:

    Input: mat = [[3, 30, 38], [20, 52, 54], [35, 60, 69]], x = 62
        Start at mat[0][2] = 38. Since 38<6238<62, move down.
        Next, check mat[1][2] = 54. Since 54<6254<62, move down.
        Finally, check mat[2][2] = 69. Since 69>6269>62, move left.
        x=62x=62 is not found, return False.

    Input: mat = [[18, 21, 27], [38, 55, 67]], x = 55
        Start at mat[0][2] = 27. Since 27<5527<55, move down.
        Next, check mat[1][2] = 67. Since 67>5567>55, move left.
        Check mat[1][1] = 55. Since 55=x55=x, return True.

    Input: mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], x = 3
        Start at mat[0][2] = 3. Since 3=x3=x, return True.

Complexity Analysis:

    Time Complexity: O(n+m), as we process at most n+mn+m elements.
    Space Complexity: O(1), as no extra space is used.



'''