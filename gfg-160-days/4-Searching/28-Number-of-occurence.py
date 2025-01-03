'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/number-of-occurrence2259

Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

Examples :

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.

Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ target ≤ 106

'''

def countOccurrences(arr, target):
    # Helper function to find the first occurrence
    def findFirst(arr, target):
        left, right = 0, len(arr) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                first = mid
                right = mid - 1  # Continue searching in the left half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    # Helper function to find the last occurrence
    def findLast(arr, target):
        left, right = 0, len(arr) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                last = mid
                left = mid + 1  # Continue searching in the right half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    # Find first and last occurrence
    first = findFirst(arr, target)
    if first == -1:  # Target is not in the array
        return 0
    last = findLast(arr, target)

    # Calculate the count of occurrences
    return last - first + 1

# Examples
print(countOccurrences([1, 1, 2, 2, 2, 2, 3], 2))  # Output: 4
print(countOccurrences([1, 1, 2, 2, 2, 2, 3], 4))  # Output: 0
print(countOccurrences([8, 9, 10, 12, 12, 12], 12))  # Output: 3

'''
Algorithm:

    Find the First Occurrence: Use binary search to find the first position (leftmost index) of the target in the array.

    Find the Last Occurrence: Use binary search to find the last position (rightmost index) of the target in the array.

    Count the Occurrences: If the target exists in the array, the count is calculated as:
    Count=(last index - first index+1)
    
    If the target is not present, the count is 0.

Explanation of the Code

    Binary Search for First Occurrence:
        If the middle element matches the target, keep searching in the left half to find the first occurrence.
        If the middle element is smaller, move to the right half.
        If the middle element is larger, move to the left half.

    Binary Search for Last Occurrence:
        If the middle element matches the target, keep searching in the right half to find the last occurrence.
        Similarly, adjust the left or right pointers based on comparisons.

    Efficiency:
        Each binary search runs in O(logn).
        Overall time complexity: O(logn), where nn is the size of the array.
        Space complexity: O(1), as no extra space is used.

Test Cases
Input:

arr = [1, 1, 2, 2, 2, 2, 3]
target = 2
'''