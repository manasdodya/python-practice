'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array

You are given an array of integers arr[]. Your task is to reverse the given array.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.

Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.

Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original.

Constraints:
1<=arr.size()<=105
'''

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        # Move the pointers
        left += 1
        right -= 1

    return arr

# Example usage
arr1 = [1, 4, 3, 2, 6, 5]
print(reverse_array(arr1))  # Output: [5, 6, 2, 3, 4, 1]

arr2 = [4, 5, 2]
print(reverse_array(arr2))  # Output: [2, 5, 4]

arr3 = [1]
print(reverse_array(arr3))  # Output: [1]

'''
Algorithm:

    Initialize Two Pointers:
        left pointing to the beginning of the array.
        right pointing to the end of the array.
    Swap Elements:
        Swap the elements at left and right.
        Increment left and decrement right to move towards the middle.
    Stop When Pointers Cross:
        Continue until left >= right.

Explanation:

    The two-pointer approach ensures that we only traverse the array once, achieving O(n) time complexity.
    The swaps are done in-place, so no additional memory is used, resulting in O(1) space complexity.

Edge Cases:

    Single Element Array: [1] remains [1].
    Empty Array: [] remains [].
    Array with Repeated Elements: [1, 1, 1] will still reverse correctly.
'''