'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/merge-two-sorted-arrays-1587115620

Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

Examples:

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10

Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output:
1 2 3 5 8 9
10 13 15 20
Explanation: After merging two sorted arrays we get 1 2 3 5 8 9 10 13 15 20.

Input: a[] = [0, 1], b[] = [2, 3]
Output:
0 1
2 3
Explanation: After merging two sorted arrays we get 0 1 2 3.

Constraints:
1 <= a.size(), b.size() <= 105
0 <= a[i], b[i] <= 107
'''
def merge_in_place(a, b):
    n, m = len(a), len(b)
    
    def next_gap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)
    
    gap = n + m
    gap = next_gap(gap)
    
    while gap > 0:
        i = 0
        
        # Compare elements in a[]
        while i + gap < n:
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
            i += 1
        
        # Compare elements in a[] and b[]
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1
        
        # Compare elements in b[]
        j = 0
        while j + gap < m:
            if b[j] > b[j + gap]:
                b[j], b[j + gap] = b[j + gap], b[j]
            j += 1
        
        gap = next_gap(gap)

# Test examples
examples = [
    ([2, 4, 7, 10], [2, 3]),
    ([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]),
    ([0, 1], [2, 3])
]

for i, (a, b) in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: a = {a}, b = {b}")
    merge_in_place(a, b)
    print(f"  Output: a = {a}, b = {b}")
    print()

'''
Algorithm: Gap Method

    Calculate Initial Gap:
        Let the initial gap be ceil((n+m)/2), where n and m are the sizes of arrays a[] and b[].

    Iterate Over Arrays:
        Compare elements separated by the gap within the combined arrays:
            If the element in a[] is greater than the element in b[], swap them.
            Adjust comparisons based on the gap position:
                Compare within a[].
                Compare across a[] and b[].
                Compare within b[].

    Reduce Gap:
        Update the gap as gap=ceil(gap/2).
        Continue until the gap becomes 0.

    Final Result:
        a[] contains the first nn smallest elements.
        b[] contains the last mm largest elements.

Explanation of Example
Input:

a = [2, 4, 7, 10], b = [2, 3]

Execution:

    Initial Gap: gap=⌈(4+2)/2⌉=3
    Compare within and across a[] and b[] with gap = 3:
        Compare a[0] with a[3]: No swap.
        Compare a[3] with b[0]: Swap 10 and 2.
        Compare b[0] with b[1]: Swap 10 and 3.
    Reduce Gap: gap=⌈3/2⌉=2gap=⌈3/2⌉=2.
    Continue comparisons:
        Swap a[1] and b[0], a[2] and b[1].
    Reduce Gap: gap=⌈2/2⌉=1.
    Continue comparisons until gap = 0.

Final Output:

a = [2, 2, 3, 4], b = [7, 10]


Time Complexity: O((n+m)log(n+m)) Gap reduces roughly by half in each iteration, and each iteration involves O(n+m)O(n+m) comparisons.

Space Complexity: O(1) The algorithm does not use additional space beyond the input arrays.

'''
