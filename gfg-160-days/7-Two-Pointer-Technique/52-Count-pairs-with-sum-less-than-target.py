'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/count-pairs-whose-sum-is-less-than-target

Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.

Examples:

Input: arr[] = [7, 2, 5, 3], target = 8
Output: 2
Explanation: There are 2 pairs with sum less than 8: (2, 5) and (2, 3). 

Input: arr[] = [5, 2, 3, 2, 4, 1], target = 5
Output: 4
Explanation: There are 4 pairs whose sum is less than 5: (2, 2), (2, 1), (3, 1) and (2, 1).

Input: arr[] = [2, 1, 8, 3, 4, 7, 6, 5], target = 7
Output: 6
Explanation: There are 6 pairs whose sum is less than 7: (2, 1), (2, 3), (2, 4), (1, 3), (1, 4) and (1, 5).

Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 104
1 <= target <= 104

'''

def countPairsWithSumLessThanTarget(arr, target):
    # Sort the array
    arr.sort()
    left, right = 0, len(arr) - 1
    count = 0

    # Two-pointer approach
    while left < right:
        if arr[left] + arr[right] < target:
            # All pairs from `left` to `right-1` are valid
            count += (right - left)
            left += 1
        else:
            right -= 1

    return count

# Example 1
arr1 = [7, 2, 5, 3]
target1 = 8
print(f"Input: arr = {arr1}, target = {target1}")
print(f"Output: {countPairsWithSumLessThanTarget(arr1, target1)}")  # Expected Output: 2

# Example 2
arr2 = [5, 2, 3, 2, 4, 1]
target2 = 5
print(f"\nInput: arr = {arr2}, target = {target2}")
print(f"Output: {countPairsWithSumLessThanTarget(arr2, target2)}")  # Expected Output: 4

# Example 3
arr3 = [2, 1, 8, 3, 4, 7, 6, 5]
target3 = 7
print(f"\nInput: arr = {arr3}, target = {target3}")
print(f"Output: {countPairsWithSumLessThanTarget(arr3, target3)}")  # Expected Output: 6

'''
Algorithm:

    Sort the Array: Sort the input array arr[] in ascending order. Sorting takes O(nlogn).
    Two-Pointer Approach:
        Initialize two pointers: left=0 (start of the array) and right=n-1 (end of the array).
        For each pair, check if arr[left]+arr[right]<target:
            If true, all pairs from leftleft to right-1 are valid (because the array is sorted).
            Increment left to check the next possible pair.
            Add right-left to the count.
            If false, decrement rightright to try smaller values.
    Return the Count: After iterating, return the total count of valid pairs.

Explanation of the Two-Pointer Technique:

    Sorting the Array:
        Sorting ensures that arr[left]+arr[right] can only increase as right moves left or left moves right.
    Why right-left?
        When arr[left]+arr[right]<target, it implies that all elements between left and right form valid pairs with arr[left].

Examples:
Example 1:

Input: arr=[7,2,5,3],target=8
Output: 22
Explanation:

    Sorted array: [2,3,5,7][2,3,5,7]
    Valid pairs: (2,5),(2,3).

Example 2:

Input: arr=[5,2,3,2,4,1],target=5
Output: 44
Explanation:

    Sorted array: [1,2,2,3,4,5][1,2,2,3,4,5]
    Valid pairs: (1,2),(1,2),(1,3),(2,2).

Example 3:

Input: arr=[2,1,8,3,4,7,6,5],target=7
Output: 66
Explanation:

    Sorted array: [1,2,3,4,5,6,7,8][1,2,3,4,5,6,7,8]
    Valid pairs: (1,2),(1,3),(1,4),(1,5),(2,3),(2,4).

Complexity Analysis:

    Time Complexity:
        Sorting the array takes O(nlogn).
        The two-pointer traversal takes O(n).
        Total: O(nlogn+n)=O(nlogn).
    Space Complexity: O(1) as we are using no additional space.
'''
