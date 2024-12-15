'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/sort-an-array-of-0s-1s-and-2s4231

Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 2

'''

def sort012(arr):
    n = len(arr)
    low, mid, high = 0, 0, n - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# Test cases
print(sort012([0, 1, 2, 0, 1, 2]))  # Output: [0, 0, 1, 1, 2, 2]
print(sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))  # Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

'''
The problem can be solved efficiently using the Dutch National Flag algorithm (also called 3-way partitioning), which sorts an array of 0s, 1s, and 2s in a single traversal with O(n) time complexity and O(1) space complexity.
Algorithm:

    Maintain three pointers:
        low for the position to place 0.
        mid for the current element being considered.
        high for the position to place 2.

    Traverse the array using the mid pointer:
        If the element is 0, swap it with the element at low and increment both low and mid.
        If the element is 1, just increment mid.
        If the element is 2, swap it with the element at high and decrement high.

    Repeat until mid surpasses high.

This ensures all 0s are moved to the left, 1s are in the middle, and 2s are moved to the right.

Explanation:

    The array is processed in one pass.
    The swaps ensure that:
        low points to the next position for 0.
        high points to the next position for 2.
        mid processes each element in the array.

Complexity:

    Time Complexity: O(n) because each element is visited at most once.
    Space Complexity: O(1) as no extra space is used.

Example Explaination
Initial Setup:

    Array: [0, 1, 2, 0, 1, 2]
    Pointers:
        low = 0: Points to the next position for 0.
        mid = 0: Points to the current element being processed.
        high = 5: Points to the next position for 2.

Step-by-Step Process:

    Iteration 1:
        mid = 0, arr[mid] = 0 (element is 0).
        Swap arr[low] and arr[mid].
        Increment both low and mid:
            low = 1, mid = 1.
        Array: [0, 1, 2, 0, 1, 2].

    Iteration 2:
        mid = 1, arr[mid] = 1 (element is 1).
        No swap needed, just increment mid:
            mid = 2.
        Array: [0, 1, 2, 0, 1, 2].

    Iteration 3:
        mid = 2, arr[mid] = 2 (element is 2).
        Swap arr[mid] and arr[high].
        Decrement high:
            high = 4.
        mid remains the same to recheck the swapped value:
            Array: [0, 1, 2, 0, 1, 2].

    Iteration 4:
        mid = 2, arr[mid] = 2 (element is 2 again after the swap).
        Swap arr[mid] and arr[high].
        Decrement high:
            high = 3.
        mid remains the same to recheck the swapped value:
            Array: [0, 1, 1, 0, 2, 2].

    Iteration 5:
        mid = 2, arr[mid] = 1 (element is 1).
        No swap needed, just increment mid:
            mid = 3.
        Array: [0, 1, 1, 0, 2, 2].

    Iteration 6:
        mid = 3, arr[mid] = 0 (element is 0).
        Swap arr[low] and arr[mid].
        Increment both low and mid:
            low = 2, mid = 4.
        Array: [0, 0, 1, 1, 2, 2].

Final State:

    Array: [0, 0, 1, 1, 2, 2].
    All 0s are at the beginning, 1s in the middle, and 2s at the end.

'''