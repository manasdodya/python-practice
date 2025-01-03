'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/kth-missing-positive-number-in-a-sorted-array

Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing from arr[].  

Examples :

Input: arr[] = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: Missing are 1, 5, 6, 8, 9, 10… and 5th missing number is 9.

Input: arr[] = [1, 2, 3], k = 2
Output: 5
Explanation: Missing are 4, 5, 6… and 2nd missing number is 5.

Input: arr[] = [3, 5, 9, 10, 11, 12], k = 2
Output: 2
Explanation: Missing are 1, 2, 4, 6… and 2nd missing number is 2.

Constraints:
1 <= arr.size() <= 105
1 <= k <= 105
1 <= arr[i]<= 106

'''

def find_kth_missing(arr, k):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    # After binary search, low points to the position where the kth missing lies
    # missing_count_before = arr[low - 1] - (low - 1 + 1) if low > 0 else 0
    return low + k

# Test examples
examples = [
    ([2, 3, 4, 7, 11], 5),
    ([1, 2, 3], 2),
    ([3, 5, 9, 10, 11, 12], 2),
]

for i, (arr, k) in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: arr={arr}, k={k}")
    print(f"  Output: {find_kth_missing(arr, k)}")
    print()



'''
Approach

    Calculate Missing Count:
        For a sorted array, the number of missing numbers before arr[i] is:
        missing=arr[i] - (i+1)
        This is because, in a perfect sequence, the i-th element would be i+1, so the difference gives the count of missing elements up to arr[i].

    Binary Search:
        Perform binary search to find the smallest index midmid such that the number of missing elements before arr[mid] is greater than or equal to kk.
        Use this index to deduce the k-th missing number.

    Handle Edge Cases:
        If k is larger than the total number of missing numbers in the array, the result lies beyond the last element.

Algorithm

    Initialize low = 0, high = len(arr) - 1.
    Use binary search to find the position:
        Compute the number of missing elements up to arr[mid].
        If the number of missing elements is less than k, move to the right.
        Otherwise, move to the left.
    After binary search, the answer can be calculated based on the missing count up to low-1.


Explanation of Example
Input: arr=[2,3,4,7,11],k=5arr=[2,3,4,7,11],k=5

    Calculate missing up to each index:
        missing[0]=2-1=1
        missing[1]=3-2=1
        missing[2]=4-3=1
        missing[3]=7-4=3
        missing[4]=11-5=6

    Binary search:
        Start low=0low=0, high=4high=4.
        mid=2mid=2, missing[2]=1missing[2]=1 (less than k=5k=5), so low=3low=3.
        mid=3mid=3, missing[3]=3missing[3]=3 (less than k=5k=5), so low=4low=4.
        mid=4mid=4, missing[4]=6missing[4]=6 (greater than k=5k=5), so high=3high=3.

    Calculate result:
        low=4low=4, so result is arr[3]+(k-missing[3])=7+(5-3)=9.

Complexity

    Time Complexity:
        Binary Search: O(log n).

    Space Complexity:
        O(1), as no additional data structures are used.
'''