'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/union-of-two-arrays3538

Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct elements from both arrays. If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements of a[] and b[] are not necessarily distinct.

Examples

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3]
Output: 5
Explanation: Union set of both the arrays will be 1, 2, 3, 4 and 5. So count is 5.

Input: a[] = [85, 25, 1, 32, 54, 6], b[] = [85, 2] 
Output: 7
Explanation: Union set of both the arrays will be 85, 25, 1, 32, 54, 6, and 2. So count is 7.

Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
Output: 2
Explanation: We need to consider only distinct. So count of elements in union set will be 2.

Constraints:
1 ≤ a.size(), b.size() ≤ 106
0 ≤ a[i], b[i] ≤ 105
'''

def countUnionElements(a, b):
    # Use a set to store unique elements
    union_set = set(a)  # Add elements of the first array
    union_set.update(b)  # Add elements of the second array
    
    # Return the size of the set
    return len(union_set)

# Test Cases
a1 = [1, 2, 3, 4, 5]
b1 = [1, 2, 3]
print(countUnionElements(a1, b1))  # Expected Output: 5

a2 = [85, 25, 1, 32, 54, 6]
b2 = [85, 2]
print(countUnionElements(a2, b2))  # Expected Output: 7

a3 = [1, 2, 1, 1, 2]
b3 = [2, 2, 1, 2, 1]
print(countUnionElements(a3, b3))  # Expected Output: 2

a4 = [0, 1, 2, 3]
b4 = [4, 5, 6]
print(countUnionElements(a4, b4))  # Expected Output: 7

a5 = []
b5 = [1, 2, 3]
print(countUnionElements(a5, b5))  # Expected Output: 3


'''
Approach:

    Use a Set to Store Unique Elements:
        Add all elements of array a[] to a set.
        Add all elements of array b[] to the same set.
        The set will automatically handle duplicate elements.
    Count the Elements in the Set:
        The size of the set will represent the number of unique elements in the union.

Time Complexity:

    Adding elements of a[] to the set: O(n)
    Adding elements of b[] to the set: O(m)
    Overall: O(n+m), where nn and mm are the sizes of a[] and b[].

Space Complexity:

    The space required for the set: O(n+m).

'''
