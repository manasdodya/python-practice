'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/count-possible-triangles-1587115620

Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle. 

    A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

Examples:

Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle.  

Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]

Input: arr[] = [1, 2, 3]
Output: 0
Explanation: No triangles are possible.

Constraints:
3 <= arr.size() <= 103
0 <= arr[i] <= 105
'''

def count_triangles(arr):
    n = len(arr)
    arr.sort()  # Sort the array
    count = 0

    # Iterate over the array from the last element (k is the largest side)
    for k in range(n - 1, 1, -1):
        i, j = 0, k - 1  # Two pointers
        while i < j:
            if arr[i] + arr[j] > arr[k]:
                # All pairs between i and j form valid triangles
                count += (j - i)
                j -= 1  # Decrease j to check for other pairs
            else:
                i += 1  # Increase i to try a larger sum

    return count

# Example Usage
arr1 = [4, 6, 3, 7]
arr2 = [10, 21, 22, 100, 101, 200, 300]
arr3 = [1, 2, 3]

print("Number of triangles (arr1):", count_triangles(arr1))  # Output: 3
print("Number of triangles (arr2):", count_triangles(arr2))  # Output: 6
print("Number of triangles (arr3):", count_triangles(arr3))  # Output: 0

'''
Algorithm

    Sort the Array
        Sort the array in ascending order. 
        This allows us to check the triangle condition efficiently because the largest element in any subset will always be the last element in the triplet.

    Two Pointers Approach for Validation
        For every possible triplet (i, j, k) where i<j<k:
            Fix the largest side as arr[k].
            Use two pointers i (starting at the beginning) and j (ending at k-1) to find pairs such that:
            arr[i] + arr[j] > arr[k]
            If valid, all pairs between i and j form valid triangles since the array is sorted. Add these pairs to the count.
            Otherwise, move the pointers appropriately to check the next set of pairs.

    Count Triangles
        Increment the triangle count for every valid triplet found.

xample Walkthrough
Example 1

Input:
arr = [4, 6, 3, 7]

    Sort the array:
    arr=[3,4,6,7]
    

    Processing triplets:
        k = 3 (largest side = 7):
            i=0,j=2: 3+6=9>7 (valid) → add j-i=2 triangles: [3,4,7], [3,6,7].
            Decrement j=1: 3+4=7≤7 (invalid). Increment i=1.
        k = 2 (largest side = 6):
            i=0,j=1: 3+4=7>6 (valid) → add j-i=1 triangle: [3,4,6].

Output:
Number of triangles = 3.
Example 2

Input:
arr = [10, 21, 22, 100, 101, 200, 300]

    Sort the array:
    arr=[10,21,22,100,101,200,300]

    Processing triplets:
        k = 6 (largest side = 300): No valid pairs.
        k = 5 (largest side = 200): Valid triangles: [100,101,200].

Output:
Number of triangles = 6.
Complexity Analysis

    Time Complexity:
        Sorting the array: O(nlogn).
        Two-pointer traversal: O(n^2) (worst-case for all k).
        Overall: O(n^2).

    Space Complexity:
        Sorting is done in-place: O(1).
'''