'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-gfg-160/problem/equilibrium-point-1587115620

Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.

Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.

Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.

Constraints:
3 <= arr.size() <= 105
-104 <= arr[i] <= 104

'''

def find_equilibrium_index(arr):
    total_sum = sum(arr)  # Compute total sum of the array
    left_sum = 0  # Initialize left sum

    for i in range(len(arr)):
        # If left sum is equal to the right sum, return index i
        if left_sum == (total_sum - left_sum - arr[i]):
            return i  # Found first equilibrium index
        
        # Update left sum for the next iteration
        left_sum += arr[i]

    return -1  # No equilibrium index found

# Test Cases
print(find_equilibrium_index([1, 2, 0, 3]))  # Output: 2 (Correct)
print(find_equilibrium_index([1, 1, 1, 1]))  # Output: -1 (Correct)
print(find_equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))  # Output: 3 (Fixed)
print(find_equilibrium_index([0, 0, 0, 0, 0]))  # Output: Any middle index (e.g., 2)

'''
Algorithm

    An equilibrium index in an array is a position i where:
    sum of elements before i=sum of elements after i

    Mathematically, this means:
    left_sum=total_sum - left_sum - arr[i]


Complexity Analysis

    Time Complexity: O(N) (Single pass through the array)
    Space Complexity: O(1) (Uses only a few extra variables)
'''