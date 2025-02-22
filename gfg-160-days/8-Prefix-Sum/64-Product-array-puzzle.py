'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-gfg-160/problem/product-array-puzzle4525

Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[].
Note: Each element is res[] lies inside the 32-bit integer range.

Examples:

Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.

Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: For i = 0, res[i] is 0.
For i = 1, res[i] is 12.

Constraints:
2 <= arr.size() <= 105
-100 <= arr[i] <= 100
'''
def product_except_self(arr):
    n = len(arr)
    if n < 2:
        return []
    
    res = [1] * n  # Initialize result array

    # Step 1: Compute prefix products
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]

    # Step 2: Compute suffix products and update result
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= arr[i]

    return res

# Test Cases
print(product_except_self([10, 3, 5, 6, 2]))  # Output: [180, 600, 360, 300, 900]
print(product_except_self([12, 0]))  # Output: [0, 12]
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]



'''
Steps:

    Compute the Prefix Product
        prefix[i] stores the product of all elements before i.
        prefix[0] = 1 (since there's nothing before index 0).
        Compute prefix[i] = prefix[i - 1] * arr[i - 1] for all i.

    Compute the Suffix Product and Fill res[] in One Pass
        suffix keeps track of the product of elements after i (initially 1).
        Traverse from right to left and update res[i] = prefix[i] * suffix.
        Update suffix = suffix * arr[i] for the next iteration.

Time Complexity

    Prefix computation: O(N)
    Suffix computation and result update: O(N)
    Total Complexity: O(N)

Space Complexity

    Extra res[] array: O(N)
    prefix and suffix variables: O(1)
    Total Complexity: O(N) (if we count res[], otherwise O(1))

Example Walkthrough
Example 1
Input:

arr = [10, 3, 5, 6, 2]
Steps:

    Prefix Products

prefix[0] = 1
prefix[1] = 1 * 10 = 10
prefix[2] = 10 * 3 = 30
prefix[3] = 30 * 5 = 150
prefix[4] = 150 * 6 = 900
res = [1, 10, 30, 150, 900]

Suffix Products and Final res[]

suffix = 1
res[4] = 900 * 1 = 900
suffix = 1 * 2 = 2

res[3] = 150 * 2 = 300
suffix = 2 * 6 = 12

res[2] = 30 * 12 = 360
suffix = 12 * 5 = 60

res[1] = 10 * 60 = 600
suffix = 60 * 3 = 180

'''