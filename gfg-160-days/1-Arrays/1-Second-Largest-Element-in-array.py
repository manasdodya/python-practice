'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735

Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.

Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

'''

def find_second_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        # Update largest and second largest if needed
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:  # Preferred condition
            second_largest = num
    
    # Return result
    return second_largest if second_largest != float('-inf') else -1

# Example usage
print(find_second_largest([12, 35, 1, 10, 34, 1]))  # Output: 34
print(find_second_largest([10, 5, 10]))            # Output: 5
print(find_second_largest([10, 10, 10]))           # Output: -1

'''
Algorithm:

    Initialize Variables:
        Set largest and second_largest to -inf (a value smaller than any element in the array).

    Traverse the Array:
        For each element in the array:
            If the element is greater than largest, update second_largest to largest, then update largest to the current element.
            Else if the element is distinct and greater than second_largest, update second_largest to the current element.

    Return the Result:
        If second_largest remains -inf (indicating no second largest distinct element exists), return -1.
        Otherwise, return second_largest.

Explanation of the Examples:

    Input: [12, 35, 1, 10, 34, 1]
        Largest = 35, Second Largest = 34.
        Output: 34.

    Input: [10, 5, 10]
        Largest = 10, Second Largest = 5.
        Output: 5.

    Input: [10, 10, 10]
        Only one distinct element (10).
        Output: -1.

Complexity Analysis:

    Time Complexity: O(n), as we traverse the array once.
    Space Complexity: O(1), as we use only two variables for tracking the largest and second largest.
'''