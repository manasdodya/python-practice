'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/maximum-product-subarray3604

Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr.

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is {-3, -10} with product = (-3) * (-10) = 30.

Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 

Constraints:
1 ≤ arr.size() ≤ 106
-10  ≤  arr[i]  ≤  10
'''

class Solution:
    def maxProduct(self, arr):
        # Initialize max_product and min_product with the first element
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        
        # Traverse through the array starting from the second element
        for i in range(1, len(arr)):
            # If the current element is negative, swap max_product and min_product
            if arr[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Update max_product and min_product
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])
            
            # Update the global result
            result = max(result, max_product)
        
        return result

# Example usage
solution = Solution()

# Test case 1
arr1 = [-2, 6, -3, -10, 0, 2]
print(solution.maxProduct(arr1))  # Output: 180

# Test case 
arr2 = [-1, -3, -10, 0, 6]
print(solution.maxProduct(arr2))  # Output: 30

# Test case 3
arr3 = [2, 3, 4]
print(solution.maxProduct(arr3))  # Output: 24


'''
Key Idea:

The challenge here arises from both positive and negative numbers in the array. The product of negative numbers can potentially become large and positive if the number of negative elements is even. Therefore, the approach will track both the maximum product (max_product) and the minimum product (min_product) at each index, because a negative value can flip a large negative product into a large positive one.
Approach:

    Initialization:
        max_product will store the maximum product found so far.
        min_product will store the minimum product (because a negative product can turn positive when multiplied by a negative number).
        Initially, both max_product and min_product are set to the first element of the array.

    Iterate through the array:
        For each element, we need to:
            If the element is negative, swap the values of max_product and min_product because multiplying a negative value can flip the signs.
            Update the max_product as the maximum of either:
                The current element itself (starting a new subarray).
                The product of the current element and the max_product (extending the current subarray).
            Similarly, update the min_product as the minimum of either:
                The current element itself (starting a new subarray).
                The product of the current element and the min_product (extending the current subarray).

    Result:
        The result is stored in max_product, which holds the largest product of any subarray encountered.
    
Explanation:

    Test Case 1:
        arr = [-2, 6, -3, -10, 0, 2]
        The subarray {6, -3, -10} gives the maximum product: 6 * -3 * -10 = 180.

    Test Case 2:
        arr = [-1, -3, -10, 0, 6]
        The subarray {-3, -10} gives the maximum product: -3 * -10 = 30.

    Test Case 3:
        arr = [2, 3, 4]
        Since all elements are positive, the maximum product is the product of all elements: 2 * 3 * 4 = 24.

Time Complexity: O(n), where n is the size of the array, because we iterate through the array only once.
Space Complexity: O(1), because we only use a constant amount of extra space for storing variables (max_product, min_product, and result).
'''