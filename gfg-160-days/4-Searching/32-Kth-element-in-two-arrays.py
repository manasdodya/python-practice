'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/k-th-element-of-two-sorted-array1317

Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

Examples :

Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

Input: a[] = [100, 112, 256, 349, 770], b[] = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256
Explanation: Combined sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element of this array is 256.

Constraints:

    1 <= a.size(), b.size() <= 106
    1 <= k <= a.size() + b.size()
    0 <= a[i], b[i] < 108

'''

# Python program to find K-th Element of Merged Two Sorted Arrays
# using Binary Search

def kthElement(a, b, k):
    n = len(a)
    m = len(b)

    # If a[] has more elements, then call kthElement
    # with reversed parameters
    if n > m:
        return kthElement(b, a, k)

    # Binary Search on the number of elements we can
    # include in the first set from a[]
    lo = max(0, k - m)
    hi = min(k, n)

    while lo <= hi:
        mid1 = (lo + hi) // 2
        mid2 = k - mid1

        # Find elements to the left and right of partition in a[]
        l1 = (mid1 == 0 and float('-inf') or a[mid1 - 1])
        r1 = (mid1 == n and float('inf') or a[mid1])

        # Find elements to the left and right of partition in b[]
        l2 = (mid2 == 0 and float('-inf') or b[mid2 - 1])
        r2 = (mid2 == m and float('inf') or b[mid2])

        # If it is a valid partition
        if l1 <= r2 and l2 <= r1:
          
            # Find and return the maximum of l1 and l2
            return max(l1, l2)

        # Check if we need to take lesser elements from a[]
        if l1 > r2:
            hi = mid1 - 1

        # Check if we need to take more elements from a[]
        else:
            lo = mid1 + 1

    return 0

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5

    print(kthElement(a, b, k))

'''
The approach is similar to the Binary Search approach of Median of two sorted arrays of different sizes.

Consider the first array is smaller. If first array is greater, then swap the arrays to make sure that the first array is smaller.
We mainly maintain two sets in this algorithm by doing binary search in the smaller array. Let mid1 be the partition of the smaller array. 
The first set contains elements from 0 to (mid1 - 1) from smaller array and mid2 = (k - mid1) elements from the greater array to make sure that the first set has exactly k elements. 
The second set contains remaining elements. 
Our target is to find a point in both arrays such that all elements in the first set are smaller than all elements in the other set (set that contains elements from right side). 
For this we validate the partitions using the same way as we did in Median of two sorted arrays of different sizes.
'''