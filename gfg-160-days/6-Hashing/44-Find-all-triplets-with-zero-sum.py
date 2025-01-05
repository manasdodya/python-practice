'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/find-all-triplets-with-zero-sum

Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero. 
Returned triplet should also be internally sorted i.e. i<j<k.

Examples:

Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation: Triplets with sum 0 are:
arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0

Input: arr[] = [1, -2, 1, 0, 5]
Output: [[0, 1, 2]]
Explanation: Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0

Input: arr[] = [2, 3, 1, 0, 5]
Output: [[]]
Explanation: There is no triplet with sum 0.

Constraints:
3 <= arr.size() <= 103
-104 <= arr[i] <= 104

'''
# Python program to find all triplets with zero sum using hashing
def findTriplets(arr):

    # Set to handle duplicates
    resSet = set()
    n = len(arr)
    mp = {}

    # Store sum of all the pairs with their indices
    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s not in mp:
                mp[s] = []
            mp[s].append((i, j))

    for i in range(n):

        # Find remaining value to get zero sum
        rem = -arr[i]
        if rem in mp:
            for p in mp[rem]:
                
                # Ensure no two indices are the same in the triplet
                if p[0] != i and p[1] != i:
                    curr = sorted([i, p[0], p[1]])
                    resSet.add(tuple(curr))

    return [list(triplet) for triplet in resSet]

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    res = findTriplets(arr)
    for triplet in res:
        print(triplet[0], triplet[1], triplet[2])


'''
The idea is to store sum of all the pairs with their indices the hash map. 
Then, for each element in the array, we check if the pair which makes triplet's sum zero, exists in the hash map or not.
Since there can be multiple valid pairs, we add each one to the hash set (to manage duplicates) while ensuring that all indices in the triplet are distinct.

time - O(n^3)
space - O(n^2)
'''