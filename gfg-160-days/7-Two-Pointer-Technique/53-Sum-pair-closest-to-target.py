'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/pair-in-array-whose-sum-is-closest-to-x1124

Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.

Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. 

Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.

Constraints:
1 <= arr.size() <= 2*105
0 <= target<= 2*105
0 <= arr[i] <= 105
'''

def closestPairWithMaxDifference(arr, target):
    if len(arr) < 2:
        return []  # Return empty array if no valid pair exists
    
    # Sort the array
    arr.sort()
    
    left, right = 0, len(arr) - 1
    closest_sum = float('inf')
    best_pair = []

    while left <= right:
        current_sum = arr[left] + arr[right]
        
        # Update the best pair if closer to target
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
            best_pair = [arr[left], arr[right]]
        elif abs(current_sum - target) == abs(closest_sum - target):
            # Choose the pair with maximum absolute difference
            if abs(arr[right] - arr[left]) > abs(best_pair[1] - best_pair[0]):
                best_pair = [arr[left], arr[right]]
        
        # Adjust pointers
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return best_pair

# Example 1
arr1 = [10, 30, 20, 5]
target1 = 25
print(f"Input: arr = {arr1}, target = {target1}")
print(f"Output: {closestPairWithMaxDifference(arr1, target1)}")  # Expected Output: [5, 20]

# Example 2
arr2 = [5, 2, 7, 1, 4]
target2 = 10
print(f"\nInput: arr = {arr2}, target = {target2}")
print(f"Output: {closestPairWithMaxDifference(arr2, target2)}")  # Expected Output: [2, 7]

# Example 3
arr3 = [10]
target3 = 10
print(f"\nInput: arr = {arr3}, target = {target3}")
print(f"Output: {closestPairWithMaxDifference(arr3, target3)}")  # Expected Output: []

# Example 4
arr4 = [1, 3, 5, 8, 10]
target4 = 15
print(f"\nInput: arr = {arr4}, target = {target4}")
print(f"Output: {closestPairWithMaxDifference(arr4, target4)}")  # Expected Output: [5, 10]


'''
Algorithm:
To solve the problem, the following steps will be followed:

    Sort the Array: Sorting helps in efficiently finding pairs using a two-pointer technique.
    Two-Pointer Technique:
        Start with one pointer at the beginning (left) and another at the end (right) of the sorted array.
        Calculate the sum of the pair and check how close it is to the target.
        If the sum is closer to the target than the current closest sum, update the closest pair.
        If multiple pairs have the same closest sum, choose the one with the maximum absolute difference.
        Adjust the pointers based on whether the sum is less than or greater than the target.
    Edge Cases: Handle cases where the array size is less than 2 by returning an empty array.

Complexity:
    This code efficiently handles the constraints using O(nlogn) time complexity for sorting and O(n) for the two-pointer traversal.

'''