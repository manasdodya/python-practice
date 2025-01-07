'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-bonus-problem/problem/count-quadruplets-with-given-sum

Given an array arr[] and an integer target, you need to find and return the count of quadruplets such that the index of each element of the quadruplet is unique and the sum of the elements is equal to target.

Examples:

Input: arr[] = [1, 5, 3, 1, 2, 10], target = 20
Output: 1
Explanation: Only quadruplet satisfying the condition is arr[1] + arr[2] + arr[4] + arr[5] = 5 + 3 + 2 + 10 = 20. Hence, the answer is 1.

Input: arr[] = [1, 1, 1, 1, 1], target = 4
Output: 5
Explanation: Three quadruplets with sum 4 are:
arr[0] + arr[1] + arr[2] + arr[3] = 1 + 1 + 1 + 1 = 4
arr[1] + arr[2] + arr[3] + arr[4] = 1 + 1 + 1 + 1 = 4
arr[0] + arr[2] + arr[3] + arr[4] = 1 + 1 + 1 + 1 = 4
arr[0] + arr[1] + arr[3] + arr[4] = 1 + 1 + 1 + 1 = 4
arr[0] + arr[1] + arr[2] + arr[4] = 1 + 1 + 1 + 1 = 4

Input: arr = [4, 3, -13, 3], target = -3
Output: 1
Explanation: There is only 1 quadruplet with sum = -3, that is [4, 3, -13, 3].

Constraints:
1 <= arr.length <= 103
-105 <=arr[i]<= 105
-105 <=target<= 105

'''

def countSum(arr, target):
    from collections import defaultdict
    count = 0
    n = len(arr)

    # Store the frequency of sum of first two elements
    m = defaultdict(int)

    # Traverse from 0 to n-1, where arr[i] is the 3rd element
    for i in range(n - 1):
      
        # All possible 4th elements
        for j in range(i + 1, n):
            temp = arr[i] + arr[j]
            count += m[target - temp]

        # Store frequency of all possible sums of first two elements
        for j in range(i):
            temp = arr[i] + arr[j]
            m[temp] += 1

    return count

# Examples
print(countSum([1, 5, 3, 1, 2, 10], 20))  # Expected: 1
print(countSum([1, 1, 1, 1, 1], 4))       # Expected: 5
print(countSum([4, 3, -13, 3], -3))       # Expected: 1

'''
    Initialize count = 0 and a hash map or dictionary to store count of all possible sums of the first two elements of possible quadruplets.
    Iterate over the array with arr[i] as the third element of the quadruplet.
    For each arr[i], loop j from [i + 1... n - 1] to find the fourth element and check if (target - arr[i] - arr[j]) exists in the hash map. If it does, add its frequency to count.
    After iterating over all possible fourth elements, traverse the array arr[] from j = 0 to i - 1 and increment the frequency of all sums arr[i] + arr[j]. 
    This is needed because when we move to the next i, we need to look for possible pairs that come before i.
    Repeat the above steps for each element arr[i] and return count as the total number of quadruplets with the given target sum.

Complexity

    Time Complexity:
        Outer for loop : O(n).
        Inner for loop: O(n).
        Hash map updates and queries: O(n).
        Overall complexity: O(n^2).

    Space Complexity:
        Hash map stores O(n^2) entries in the worst case.
'''