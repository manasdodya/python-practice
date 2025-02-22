'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-bonus-problem/problem/largest-rectangular-sub-matrix-whose-sum-is-0

Given a matrix mat[][]. Find the size of the largest sub-matrix whose sum is equal to zero. The size of a matrix is the product of rows and columns. A sub-matrix is a matrix obtained from the given matrix by deletion of several (possibly, zero or all) rows/columns from the beginning and several (possibly, zero or all) rows/columns from the end.

Examples:

Input: mat[][] = [[9, 7, 16, 5], [1, -6, -7, 3], [1, 8, 7, 9], [7, -2, 0, 10]] 
Output: 6
Explanation: 

Input: mat[][] =  [[1, 2, 3], [-3, -2, -1], [1, 7, 5]]
Output:  6
Explanation:

Input: mat[][] = [[1, -1], [-1, 1]]
Output: 4
Explanation: The largest sub-matrix with sum 0 is [[1, -1], [-1, 1]].

Constraints:
1 <= mat.size(), mat[0].size() <= 100
-1000 <= mat[][] <= 1000
'''

def largestZeroSumSubmatrix(mat):
    if not mat or not mat[0]: 
        return 0

    rows, cols = len(mat), len(mat[0])
    max_size = 0

    # Iterate over all possible row pairs
    for r1 in range(rows):
        col_prefix = [0] * cols  # Column-wise prefix sum
        
        for r2 in range(r1, rows):
            # Compute column-wise prefix sum between row r1 and r2
            for c in range(cols):
                col_prefix[c] += mat[r2][c]

            # Now, find the largest subarray with sum zero in col_prefix
            prefix_map = {0: -1}  # Initialize for sum zero at start
            curr_sum = 0

            for c in range(cols):
                curr_sum += col_prefix[c]

                if curr_sum in prefix_map:
                    width = c - prefix_map[curr_sum]
                    height = r2 - r1 + 1
                    max_size = max(max_size, width * height)
                else:
                    prefix_map[curr_sum] = c  # Store first occurrence
            
    return max_size

# Example Test Cases
mat1 = [[9, 7, 16, 5], 
        [1, -6, -7, 3], 
        [1, 8, 7, 9], 
        [7, -2, 0, 10]]

mat2 = [[1, 2, 3], 
        [-3, -2, -1], 
        [1, 7, 5]]

mat3 = [[1, -1], 
        [-1, 1]]

print(largestZeroSumSubmatrix(mat1))  # Output: 6
print(largestZeroSumSubmatrix(mat2))  # Output: 6
print(largestZeroSumSubmatrix(mat3))  # Output: 4

'''
Algorithm Explanation

The problem requires finding the largest sub-matrix whose sum is exactly zero. The size of the sub-matrix is calculated as the product of the number of rows and columns.
Efficient Approach (Prefix Sum + Hash Map)

    Convert the Problem to a 1D Subarray Sum Zero Problem:
        Fix two row boundaries (r1 and r2) and collapse the matrix into a 1D prefix sum array for the columns.
        Finding a sub-matrix with sum zero now reduces to finding a subarray with sum zero in this collapsed array.

    Use Hash Map to Track Column Prefix Sums:
        Iterate through all possible row boundaries.
        Maintain column-wise prefix sums and use a hash map to track the first occurrence of each sum.
        If the same prefix sum occurs again at different columns, the subarray between these columns has sum zero.

    Track Maximum Sub-matrix Size:
        Update the maximum area found based on the number of rows (r2 - r1 + 1) and number of columns contributing to sum zero.

Example Walkthrough
Example 1

Input:

mat = [[9, 7, 16, 5], 
       [1, -6, -7, 3], 
       [1, 8, 7, 9], 
       [7, -2, 0, 10]]

    The largest sub-matrix with sum zero has a size of 6.

Example 2

Input:

mat = [[1, 2, 3], 
       [-3, -2, -1], 
       [1, 7, 5]]

    Largest zero-sum sub-matrix has size 6.

Example 3

Input:

mat = [[1, -1], 
       [-1, 1]]

    The entire matrix sums to 0, so output is 4.

Complexity Analysis

    Outer Loop: O(R) for selecting r1.
    Inner Loop: O(R) for selecting r2.
    Column-wise Sum Calculation: O(C).
    Finding Largest Zero-Sum Subarray: O(C) using a hash map.

Total Complexity:
O(R^2⋅C)
This is efficient for R,C ≤100 as the worst case is 100^3=10^6, which is feasible.
'''