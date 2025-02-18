'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-bonus-problems/problem/triplet-sum-in-array-1587115621

Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

Return true if such a triplet exists, otherwise, return false.

Examples

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13 
Output: true 
Explanation: The triplet {1, 4, 8} sums up to 13

Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10 
Output: true 
Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10. 

Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24 
Output: false 
Explanation: No triplet in the array sums to 24

Constraints:
3 ≤ arr.size() ≤ 103
1 ≤ arr[i] ≤ 105
'''

def find_triplet_with_sum(arr, target):
    # Step 1: Sort the array
    arr.sort()
    n = len(arr)
    
    # Step 2: Iterate through the array
    for i in range(n - 2):
        # Initialize two pointers
        left, right = i + 1, n - 1
        
        while left < right:
            # Calculate current sum
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                return True  # Triplet found
            elif current_sum < target:
                left += 1  # Increase sum by moving left pointer
            else:
                right -= 1  # Decrease sum by moving right pointer
    
    # No triplet found
    return False

# Example Usage
arr1 = [1, 4, 45, 6, 10, 8]
target1 = 13
arr2 = [1, 2, 4, 3, 6, 7]
target2 = 10
arr3 = [40, 20, 10, 3, 6, 7]
target3 = 24

print("Output for arr1:", find_triplet_with_sum(arr1, target1))  # Output: True
print("Output for arr2:", find_triplet_with_sum(arr2, target2))  # Output: True
print("Output for arr3:", find_triplet_with_sum(arr3, target3))  # Output: False

'''
Algorithm: Two-Pointer Technique

    Sort the Array:
        Sort the array in ascending order. This helps in efficiently finding the triplet sum using two pointers.

    Iterate Through the Array:
        For each element in the array, treat it as the first element of the triplet.

    Use Two Pointers:
        Initialize two pointers: left pointing to the element after the current one and right pointing to the last element.
        Calculate the sum of the triplet:
        current_sum=arr[i]+arr[left]+arr[right]
        current_sum=arr[i]+arr[left]+arr[right]
        If current_sum == target, return True.
        If current_sum < target, move the left pointer to the right to increase the sum.
        If current_sum > target, move the right pointer to the left to decrease the sum.

    No Triplet Found:
        If no triplet is found after iterating through the array, return False.
    
Example Walkthrough
Input: arr = [1, 4, 45, 6, 10, 8], target = 13

    Sort the Array:
        Sorted arr = [1, 4, 6, 8, 10, 45].

    First Iteration (i = 0, arr[i] = 1):
        left = 1 (arr[1] = 4), right = 5 (arr[5] = 45).
        Check: 1+4+45=50, move right.
        Check: 1+4+10=15, move right.
        Check: 1+4+8=13, return True.

Complexity Analysis

    Time Complexity:
        Sorting the array: O(nlogn).
        Two-pointer search for each element: O(n2).
        Overall complexity: O(n2).

    Space Complexity:
        Sorting is done in place, so no extra space is used: O(1).

Edge Cases

    Minimum Array Size:
        Input: arr = [1, 2, 3], target = 6.
        Output: True.

    No Triplet:
        Input: arr = [5, 5, 5], target = 20.
        Output: False.

    All Elements Equal:
        Input: arr = [1, 1, 1, 1], target = 3.
        Output: True.

    Large Inputs:
        Efficient for 3≤n≤1033≤n≤103.

'''