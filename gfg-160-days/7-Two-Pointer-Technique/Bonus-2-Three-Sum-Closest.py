'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-bonus-problems/problem/3-sum-closest

Given an array arr[] and an integer target, the task is to find the sum of three integers in arr[] such that the sum is closest to target. 

Note: If multiple sums are closest to target, return the maximum one.

Examples:

Input: arr[] = [-1, 2, 2, 4], target = 4
Output: 5
Explanation: All possible triplets
[-1, 2, 2], sum = (-1) + 2 + 2 = 3
[-1, 2, 4], sum = (-1) + 2 + 4 = 5
[-1, 2, 4], sum = (-1) + 2 + 4 = 5
[2, 2, 4], sum = 2 + 2 + 4 = 8
Triplet [-1, 2, 2], [-1, 2, 4] and [-1, 2, 4] have sum closest to target, so return the maximum one, that is 5.

Input: arr[] = [1, 10, 4, 5], target = 10
Output: 10
Explanation: All possible triplets
[1, 10, 4], sum = (1 + 10 + 4) = 15
[1, 10, 5], sum = (1 + 10 + 5) = 16
[1, 4, 5], sum = (1 + 4 + 5) = 10
[10, 4, 5], sum = (10 + 4 + 5) = 19 
Triplet [1, 4, 5] has sum = 10 which is closest to target.

Constraints:
3 <= arr.size() <= 103
-103 ≤ arr[i] ≤ 103
-104 ≤ target ≤ 104

'''

def closest_three_sum(arr, target):
    # Step 1: Sort the array
    arr.sort()
    n = len(arr)
    
    # Step 2: Initialize variables
    closest_sum = float('-inf')
    min_diff = float('inf')
    
    # Step 3: Iterate through the array
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            diff = abs(target - current_sum)

            # If an exact match is found, return it
            if current_sum == target:
                return current_sum
            
            # Check if the current sum is closer to the target
            if diff < min_diff or (diff == min_diff and current_sum > closest_sum):
                min_diff = diff
                closest_sum = current_sum
            
            # Move pointers based on sum comparison
            if current_sum < target:
                left += 1  # Increase sum
            else:
                right -= 1  # Decrease sum

    # Step 4: Return the closest sum
    return closest_sum

# Example Test Cases
print(closest_three_sum([-1, 2, 2, 4], 4))  # Output: 5
print(closest_three_sum([1, 10, 4, 5], 10)) # Output: 10
print(closest_three_sum([-5, -2, 1, 3, 7], 6)) # Output: 6
print(closest_three_sum([0, 0, 0], 1)) # Output: 0


'''
Algorithm

    Sort the Array: Sorting allows efficient searching with the two-pointer approach.
    Iterate through the Array:
        For each element at index i, use two pointers: left = i + 1 and right = n - 1.
        Compute the sum of the triplet:
        current_sum=arr[i]+arr[left]+arr[right]
        If current_sum is exactly target, return target as it's the closest possible sum.
        Keep track of the closest sum found so far.
        If there are multiple sums with the same absolute difference from target, return the maximum one.
        If current_sum < target, move left to the right to increase the sum.
        If current_sum > target, move right to the left to decrease the sum.
    Return the closest maximum sum.

    
Example Walkthrough
Input: arr = [-1, 2, 2, 4], target = 4
Sorted Array: [-1, 2, 2, 4]
All Possible Triplets:

    (-1, 2, 2) → sum = 3
    (-1, 2, 4) → sum = 5
    (2, 2, 4) → sum = 8
    Closest sums to 4: {3, 5, 5}
    Maximum among them: 5

Output: 5
Complexity Analysis

    Sorting the Array: O(nlogn)
    Iterating with Two Pointers: O(n2)
    Overall Time Complexity: O(n2)
    Space Complexity: O(1) (no extra space used)
'''