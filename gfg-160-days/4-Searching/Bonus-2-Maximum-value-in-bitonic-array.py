'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-bonus-problems/problem/maximum-value-in-a-bitonic-array3001

Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.

Examples:

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].

Input: arr[] = [10, 20, 30, 40, 50]
Output: 50
Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.

Input: arr[] = [120, 100, 80, 20, 0]
Output: 120
Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].

Constraints:
3 ≤ arr.size() ≤ 105
1 ≤ arr[i]≤ 106

'''

def find_bitonic_point(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check for the bitonic point
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
            return arr[mid]

        # If the mid is in the increasing part
        if mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:  # mid is in the decreasing part
            high = mid - 1

    return -1  # Should never reach here

# Test examples
examples = [
    [1, 2, 4, 5, 7, 8, 3],
    [10, 20, 30, 40, 50],
    [120, 100, 80, 20, 0],
    [1, 3, 8, 12, 4, 2],
    [10, 9, 8, 7]
]

for i, arr in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: {arr}")
    print(f"  Bitonic Point: {find_bitonic_point(arr)}")
    print()

'''
Approach

    Binary Search:
        The maximum element in a bitonic array is greater than its neighbors.
        Check the mid-point arr[mid]arr[mid]:
            If arr[mid]>arr[mid - 1] and arr[mid]>arr[mid + 1], arr[mid] is the bitonic point.
            If arr[mid]>arr[mid - 1] but arr[mid]<arr[mid + 1], the maximum lies to the right (low=mid+1).
            If arr[mid]<arr[mid - 1], the maximum lies to the left (high=mid-1).

    Termination:
        The search ends when low==high, at which point arr[low] is the maximum element.

    Constraints Handling:
        Ensure mid - 1 and mid + 1 indices are within bounds.

        
Explanation of Example
Input: arr=[1,2,4,5,7,8,3]

    Perform binary search:
        low=0,high=6,mid=3, arr[3]=5:
            arr[3]<arr[4], so move low=4.
        low=4,high=6,mid=5, arr[5]=8:
            arr[5]>arr[4] and arr[5]>arr[6], so arr[5]=8 is the bitonic point.

    Output: 8.

Complexity

    Time Complexity:
        Binary search operates in O(logn), where nn is the size of the array.

    Space Complexity:
        O(1), as no additional data structures are used.

Edge Cases

    Fully Increasing Array:
        Input: [10,20,30,40,50]
        Output: 50 (last element).

    Fully Decreasing Array:
        Input: [120,100,80,20,0]
        Output: 120 (first element).
'''