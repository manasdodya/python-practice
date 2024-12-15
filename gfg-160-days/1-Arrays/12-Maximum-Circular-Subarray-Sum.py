'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620

Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.

Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].

Input: arr[] = [-1, 40, -14, 7, 6, 5, -4, -1] 
Output: 52
Explanation: Circular Subarray [7, 6, 5, -4, -1, -1, 40] has the maximum sum, which is 52.

Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
'''

def circularSubarraySum(arr):
    # Initialize variables
    totalSum = 0
    currMax = 0
    currMin = 0
    maxSum = arr[0]
    minSum = arr[0]
    
    for i in range(len(arr)):
        # Update current max subarray sum using Kadane's algorithm
        currMax = max(currMax + arr[i], arr[i])
        maxSum = max(currMax, maxSum)
        
        # Update current min subarray sum using Kadane's algorithm
        currMin = min(currMin + arr[i], arr[i])
        minSum = min(currMin, minSum)
        
        # Add current element to the total sum
        totalSum += arr[i]
    
    # Calculate circular subarray sum: total sum minus minimum subarray sum
    circularSum = totalSum - minSum
    
    # If all elements are negative, then the circular sum will be the same as the max subarray sum
    if minSum == totalSum:
        return maxSum
    
    # Return the maximum of non-circular and circular subarray sums
    return max(maxSum, circularSum)

# Test the function with example cases
arr1 = [8, -8, 9, -9, 10, -11, 12]
print(circularSubarraySum(arr1))  # Output: 22

arr2 = [10, -3, -4, 7, 6, 5, -4, -1]
print(circularSubarraySum(arr2))  # Output: 23

arr3 = [-1, 40, -14, 7, 6, 5, -4, -1]
print(circularSubarraySum(arr3))  # Output: 52

