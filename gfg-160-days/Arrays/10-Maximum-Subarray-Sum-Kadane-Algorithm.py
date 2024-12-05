'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620

Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

Constraints:
1 ≤ arr.size() ≤ 105
-109 ≤ arr[i] ≤ 104
'''

class Solution:
    def maxSubArray(self, arr):
        # Initialize variables
        max_sum = arr[0]
        current_sum = arr[0]
        
        # Traverse the array starting from the second element
        for i in range(1, len(arr)):
            # Update current_sum to the maximum of current element or current_sum + arr[i]
            current_sum = max(arr[i], current_sum + arr[i])
            
            # Update max_sum to the maximum of max_sum or current_sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Example usage
solution = Solution()

# Test case 1
arr1 = [2, 3, -8, 7, -1, 2, 3]
print(solution.maxSubArray(arr1))  # Output: 11

# Test case 2
arr2 = [-2, -4]
print(solution.maxSubArray(arr2))  # Output: -2

# Test case 3
arr3 = [5, 4, 1, 7, 8]
print(solution.maxSubArray(arr3))  # Output: 25

'''
Kadane's Algorithm:

The basic idea of Kadane's Algorithm is to keep track of the maximum sum of the subarray that ends at the current index and then update the global maximum sum. At each step, we decide whether to:

    Add the current element to the existing subarray sum.
    Start a new subarray from the current element if it's better than including the current element in the existing subarray.

Steps:

    Initialization:
        max_sum to store the global maximum subarray sum.
        current_sum to store the current subarray sum as we traverse the array.

    Traverse the Array:
        At each element, update the current_sum as the maximum of either the current element or the sum of the current element and the previous subarray sum (current_sum + arr[i]).
        Update max_sum if current_sum exceeds max_sum.

    Edge Case: If all elements are negative, the maximum subarray sum will be the largest single element.

Explanation:

    Test Case 1:
        arr = [2, 3, -8, 7, -1, 2, 3]
        Subarray {7, -1, 2, 3} gives the maximum sum 11.

    Test Case 2:
        arr = [-2, -4]
        The maximum sum is -2 since all values are negative.

    Test Case 3:
        arr = [5, 4, 1, 7, 8]
        The subarray {5, 4, 1, 7, 8} gives the maximum sum 25.

Time Complexity: O(n), where n is the size of the array. We only need to iterate through the array once.
Space Complexity: O(1), because we only use a constant amount of extra space (max_sum and current_sum).

'''