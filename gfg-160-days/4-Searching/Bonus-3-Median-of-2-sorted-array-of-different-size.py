'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-bonus-problems/problem/median-of-2-sorted-arrays-of-different-sizes

Given two sorted arrays a[] and b[], . You need to find and return the median of the combined array after merging them into a single sorted array.

Examples:

Input: a[] = [-5, 3, 6, 12, 15], b[] = [-12, -10, -6, -3, 4, 10]
Output: 3
Explanation: The merged array is [-12, -10, -6, -5, -3, 3, 4, 6, 10, 12, 15]. So the median of the merged array is 3.

Input: a[] = [2, 3, 5, 8], b[] = [10, 12, 14, 16, 18, 20]
Output: 11
Explanation: The merged array is [2, 3, 5, 8, 10, 12, 14, 16, 18, 20]. So the median of the merged array is (10 + 12) / 2 = 11.

Input: a[] = [], b[] = [2, 4, 5, 6]
Output: 4.5
Explanation: The merged array is [2, 4, 5, 6]. So the median of the merged array is (4 + 5) / 2 = 4.5.

Constraints: 
0 ≤ a.size(), b.size() ≤ 106
1 ≤ a[i], b[i] ≤ 109
a.size() + b.size() > 0

'''

def find_median_sorted_arrays(a, b):
    # Ensure a is the smaller array
    if len(a) > len(b):
        a, b = b, a

    m, n = len(a), len(b)
    low, high = 0, m

    while low <= high:
        partitionA = (low + high) // 2
        partitionB = (m + n + 1) // 2 - partitionA

        # Edge cases: if partition is at the boundary
        maxLeftA = float('-inf') if partitionA == 0 else a[partitionA - 1]
        minRightA = float('inf') if partitionA == m else a[partitionA]

        maxLeftB = float('-inf') if partitionB == 0 else b[partitionB - 1]
        minRightB = float('inf') if partitionB == n else b[partitionB]

        # Check if partition is correct
        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            # Median calculation
            if (m + n) % 2 == 0:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                return max(maxLeftA, maxLeftB)
        elif maxLeftA > minRightB:
            high = partitionA - 1
        else:
            low = partitionA + 1

    # If the input arrays are not valid
    return -1

# Test examples
examples = [
    ([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]),
    ([2, 3, 5, 8], [10, 12, 14, 16, 18, 20]),
    ([], [2, 4, 5, 6])
]

for i, (a, b) in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Array A: {a}")
    print(f"  Array B: {b}")
    print(f"  Median: {find_median_sorted_arrays(a, b)}")
    print()


'''
Approach

    Binary Search on the Smaller Array:
        Perform binary search on one of the arrays (preferably the smaller one to minimize time complexity).

    Partitioning:
        Divide both arrays into two parts such that the left part of both arrays combined contains half of the total elements (or one extra for odd-sized arrays).

    Median Conditions:
        Ensure that the maximum of the left parts is less than or equal to the minimum of the right parts:
            maxLeftA≤minRightBmaxLeftA≤minRightB
            maxLeftB≤minRightAmaxLeftB≤minRightA

    Median Calculation:
        If the total number of elements is even:
        Median=max⁡(maxLeftA,maxLeftB)+min⁡(minRightA,minRightB)2
        Median=2max(maxLeftA,maxLeftB)+min(minRightA,minRightB)​
        If the total number of elements is odd:
        Median=max⁡(maxLeftA,maxLeftB)
        Median=max(maxLeftA,maxLeftB)

    Adjusting Binary Search:
        If maxLeftA>minRightBmaxLeftA>minRightB, move the partition in aa to the left.
        If maxLeftB>minRightAmaxLeftB>minRightA, move the partition in aa to the right.


Explanation of Example
Input:

    a=[−5,3,6,12,15]a=[−5,3,6,12,15], b=[−12,−10,−6,−3,4,10]b=[−12,−10,−6,−3,4,10]

    m=5,n=6m=5,n=6; aa is already smaller, so proceed with binary search on aa.

    Partition the arrays:
        partitionA=2,partitionB=4partitionA=2,partitionB=4
        maxLeftA=3,minRightA=6maxLeftA=3,minRightA=6
        maxLeftB=−3,minRightB=4maxLeftB=−3,minRightB=4

    Adjust binary search:
        maxLeftA≤minRightBmaxLeftA≤minRightB and maxLeftB≤minRightAmaxLeftB≤minRightA, so the partition is correct.

    Calculate the median:
        (m+n)%2=1(m+n)%2=1 (odd total size), so:
        Median=max⁡(maxLeftA,maxLeftB)=max⁡(3,−3)=3
        Median=max(maxLeftA,maxLeftB)=max(3,−3)=3

Complexity

    Time Complexity:
        O(log⁡(min⁡(m,n)))O(log(min(m,n))), as binary search is performed on the smaller array.

    Space Complexity:
        O(1)O(1), as no extra space is used.
'''