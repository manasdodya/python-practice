'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/spirally-traversing-a-matrix-1587115621

You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

Examples:

Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
Explanation: 

Input: mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
Explanation: Applying same technique as shown above.

Input: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
Output: [32, 44, 27, 23, 62, 50, 28, 54]
Explanation: Applying same technique as shown above, output will be [32, 44, 27, 23, 62, 50, 28, 54].

Constraints:
1 <= n, m <= 1000
0 <= mat[i][j]<= 100

'''

def spiral_order(mat):
    if not mat or not mat[0]:
        return []
    
    n, m = len(mat), len(mat[0])
    top, bottom, left, right = 0, n - 1, 0, m - 1
    result = []
    
    while top <= bottom and left <= right:
        # Traverse the top row
        for col in range(left, right + 1):
            result.append(mat[top][col])
        top += 1
        
        # Traverse the right column
        for row in range(top, bottom + 1):
            result.append(mat[row][right])
        right -= 1
        
        if top <= bottom:
            # Traverse the bottom row
            for col in range(right, left - 1, -1):
                result.append(mat[bottom][col])
            bottom -= 1
        
        if left <= right:
            # Traverse the left column
            for row in range(bottom, top - 1, -1):
                result.append(mat[row][left])
            left += 1
    
    return result

# Test examples
examples = [
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]],
    [[32, 44, 27, 23], [54, 28, 50, 62]],
]

for i, mat in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"Input: {mat}")
    print(f"Output: {spiral_order(mat)}")
    print()


'''
Algorithm

    Define Boundaries:
        Start with top=0top=0, bottom=n−1bottom=n−1, left=0left=0, right=m−1right=m−1.

    Traverse the Matrix:
        Traverse the top row from leftleft to rightright and increment toptop.
        Traverse the right column from toptop to bottombottom and decrement rightright.
        Traverse the bottom row from rightright to leftleft and decrement bottombottom (if top≤bottomtop≤bottom).
        Traverse the left column from bottombottom to toptop and increment leftleft (if left≤rightleft≤right).

    Repeat Until Complete:
        Continue the process while top≤bottomtop≤bottom and left≤rightleft≤right.

    Return the Result:
        Collect the elements in a list and return it.
    
Explanation of Examples
Input:

    mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

Spiral Traversal:

    Traverse the top row: [1,2,3,4]
    Traverse the right column: [8,12,16]
    Traverse the bottom row: [15,14,13]
    Traverse the left column: [9,5]
    Traverse the inner top row: [6,7]
    Traverse the inner bottom row: [11,10]

Output:

    [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

Complexity

    Time Complexity:
        O(n⋅m): Each element is visited exactly once.

    Space Complexity:
        O(1): The result array does not count as additional space.

'''