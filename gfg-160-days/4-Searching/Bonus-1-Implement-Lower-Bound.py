'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-bonus-problems/problem/implement-lower-bound

Given a sorted array arr[] and a number target, the task is to find the lower bound of the target in this given array. The lower bound of a number is defined as the smallest index in the sorted array where the element is greater than or equal to the given number.

Note: If all the elements in the given array are smaller than the target, the lower bound will be the length of the array. 

Examples :

Input:  arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
Output: 3
Explanation: 3 is the smallest index in arr[] where element (arr[3] = 10) is greater than or equal to 9.

Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 11
Output: 4
Explanation: 4 is the smallest index in arr[] where element (arr[4] = 11) is greater than or equal to 11.

Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 100
Output: 7
Explanation: As no element in arr[] is greater than 100, return the length of array.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ target ≤ 106

'''

def find_lower_bound(arr, target):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1

    # At the end, 'low' is the smallest index where arr[low] >= target
    return low

# Test examples
examples = [
    ([2, 3, 7, 10, 11, 11, 25], 9),
    ([2, 3, 7, 10, 11, 11, 25], 11),
    ([2, 3, 7, 10, 11, 11, 25], 100)
]

for i, (arr, target) in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: arr={arr}, target={target}")
    print(f"  Output: {find_lower_bound(arr, target)}")
    print()




'''
Approach

    Binary Search:
        Use binary search to find the smallest index ii such that arr[i]≥targetarr[i]≥target.
        If no such index exists (all elements are smaller), return the length of the array.

    Procedure:
        Initialize low=0low=0 and high=len(arr)-1high=len(arr)-1.
        Use the mid-point to decide:
            If arr[mid]≥targetarr[mid]≥target, move high=mid-1high=mid-1, as the potential answer is midmid or an earlier index.
            If arr[mid]<targetarr[mid]<target, move low=mid+1low=mid+1, as the answer lies to the right.
        At the end, lowlow will point to the lower bound.

    Edge Cases:
        If all elements are smaller than targettarget, lowlow will exceed the array bounds, and we return len(arr)len(arr).

        
Explanation of Example
Input: arr=[2,3,7,10,11,11,25],target=9

    Perform binary search:
        low=0,high=6,mid=3, arr[3]=10≥9, so high=2high=2.
        low=0,high=2,mid=1, arr[1]=3<9, so low=2low=2.
        low=2,high=2,mid=2, arr[2]=7<9, so low=3low=3.

    At the end, low=3low=3, which is the smallest index where arr[3]≥9.

    Output: 33.

Complexity

    Time Complexity:
        Binary search operates in O(logn), where nn is the size of the array.

    Space Complexity:
        O(1), as no additional data structures are used.

Edge Case
Input: arr=[2,3,7,10,11,11,25],target=100

    Binary search ends with low=7low=7, as no element satisfies arr[i]≥100.
    Output: 77 (length of the array).
'''