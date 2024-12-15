'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/inversion-of-array-1587115620

Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

    Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
    If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.

Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
'''
def merge_and_count(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0

    # Merge two sorted halves and count inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inv_count += (mid - i + 1)  # Count inversions
        k += 1

    # Copy remaining elements from left subarray
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right subarray
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy sorted subarray back to original array
    arr[left:right + 1] = temp[left:right + 1]

    return inv_count

def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        # Count inversions in left and right halves
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)

        # Count split inversions during merge
        inv_count += merge_and_count(arr, temp, left, mid, right)

    return inv_count

def inversion_count(arr):
    n = len(arr)
    temp = [0] * n  # Allocate temp array once
    return merge_sort_and_count(arr, temp, 0, n - 1)


print(inversion_count([2,4,1,3,5])) # output = 3
print(inversion_count([2,3,4,5,6])) # output = 0
print(inversion_count([10,10,10])) # output = 0
print(inversion_count([5,3,2,1,0])) # output =  
print(inversion_count([1,20,6,4,5])) # output = 

'''
Algorithm

    Initialization:
        Define a helper function merge_and_count to merge two sorted halves of the array and count inversions during the merge step.
        Define another function merge_sort_and_count that recursively divides the array into smaller parts and calculates inversion counts using merge_and_count.

    Divide and Conquer:
        In merge_sort_and_count:
            Split the array into two halves (left and right).
            Recursively count inversions in the left half.
            Recursively count inversions in the right half.
            Count the inversions across the two halves using merge_and_count.

    Merging:
        In merge_and_count:
            Compare elements from the two halves.
            If an element in the left half is greater than an element in the right half, count inversions for all remaining elements in the left half (since they will all be greater than the current element in the right half).
            Merge the two halves back into a sorted order.

    Return Results:
        The final inversion count is obtained after processing the entire array through recursive division and merging.


Expected Results
Input:

    arr = [2, 4, 1, 3, 5]

Output:

    Inversion Count: 3

Explanation of One Result
Example:

Input: arr = [2, 4, 1, 3, 5]

Step-by-step Execution:

    Split array into [2, 4, 1] and [3, 5].
    Process [2, 4, 1]:
        Split into [2, 4] and [1].
        Count inversions in [2, 4] (none).
        Merge [2, 4] and [1]:
            1 is less than 2 and 4, resulting in 2 inversions.
        Result: [1, 2, 4] with 2 inversions.
    Process [3, 5] (no inversions).
    Merge [1, 2, 4] and [3, 5]:
        3 and 5 are greater than all elements in [1, 2, 4], so no new inversions.
        Result: [1, 2, 3, 4, 5] with 1 more inversion from earlier.
    Total inversions: 2 + 0 + 1 = 3.

Explanation of Time and Space Complexity
Time Complexity:

    The merge sort algorithm divides the array into halves at each recursive step, creating a recursion tree with a height of log n.
    At each level, merging takes O(n)O(n), as every element is processed once.
    Total time complexity: O(nlog n).

Space Complexity:

    A temporary array (temp) of size nn is used for merging.
    Space complexity: O(n) for the temp array.
    No additional space is used for recursion since the recursion depth is O(log n) (not counted as additional memory in most complexity analyses).

'''