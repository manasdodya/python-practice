'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/intersection-of-two-arrays-with-duplicate-elements

Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not have duplicate elements and the result should contain items in any order.

Note: The driver code will sort the resulting array in increasing order before printing.

Examples:

Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
Output: [1, 3]
Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.

Input: a[] = [1, 1, 1], b[] = [1, 1, 1, 1, 1]
Output: [1]
Explanation: 1 is the only common element present in both the arrays.

Input: a[] = [1, 2, 3], b[] = [4, 5, 6]
Output: []
Explanation: No common element in both the arrays.

Constraints:
1 ≤ a.size(), b.size() ≤ 105
1 ≤ a[i], b[i] ≤ 105
'''
def findIntersection(a, b):
    # Convert both arrays to sets to remove duplicates
    set_a = set(a)
    set_b = set(b)
    
    # Find intersection of the two sets
    intersection = set_a & set_b  # or use set_a.intersection(set_b)
    
    # Convert the set to a list and return
    return list(intersection)

# Test Cases
a1 = [1, 2, 1, 3, 1]
b1 = [3, 1, 3, 4, 1]
print(findIntersection(a1, b1))  # Expected: [1, 3] (order doesn't matter)

a2 = [1, 1, 1]
b2 = [1, 1, 1, 1, 1]
print(findIntersection(a2, b2))  # Expected: [1]

a3 = [1, 2, 3]
b3 = [4, 5, 6]
print(findIntersection(a3, b3))  # Expected: []

a4 = [1, 2, 3, 4, 5]
b4 = [3, 4, 5, 6, 7]
print(findIntersection(a4, b4))  # Expected: [3, 4, 5]


'''
Approach:

    Use Sets:
        Convert both arrays to sets to remove duplicates.
        Compute the intersection of the two sets using the & operator or the intersection() method.
    Return the Result:
        Convert the resulting set to a list.
        The driver code will handle sorting before printing.

Time Complexity:

    Converting an array to a set: O(n)
    Finding the intersection of two sets: O(min(m,n)), where m and n are the sizes of the two arrays.
    Overall time complexity: O(n+m).

Space Complexity:

    Using sets for both arrays: O(n+m).


'''