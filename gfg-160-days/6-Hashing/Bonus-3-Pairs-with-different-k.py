'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-bonus-problem/problem/pairs-with-difference-k1713

Given an array arr[] of positive integers. Find the number of pairs of integers whose absolute difference equals to a given number k.
Note: (a, b) and (b, a) are considered the same. Also, the same numbers at different indices are considered different.

The answer is guaranteed to fit in a 32-bit integer.

Examples:

Input: arr[] = [1, 4, 1, 4, 5], k = 3
Output: 4
Explanation: There are 4 pairs with absolute difference 3, the pairs are {1, 4}, {1, 4}, {4, 1} and {1, 4}.

Input: arr[] = [8, 16, 12, 16, 4, 0], k = 4
Output: 5
Explanation: There are 5 pairs with absolute difference 4, the pairs are {8, 12}, {8, 4}, {16, 12}, {12, 16}, {4, 0}.

Constraints:
1 <= arr.size() <= 2*105
1 <= k <= 2*105
0 <= arr[i] <= 105
'''

def countPairsWithDiffK(arr, k):
    n = len(arr)  
    freq = {}
    cnt = 0

    for i in range(n):
      
        # Check if the complement (arr[i] + k)
        # exists in the map. If yes, increment count
        if (arr[i] + k) in freq: 
            cnt += freq[arr[i] + k] 
      
        # Check if the complement (arr[i] - k)
        # exists in the map. If yes, increment count
        if (arr[i] - k) in freq: 
            cnt += freq[arr[i] - k] 
      
        # Increment the frequency of arr[i]
        freq[arr[i]] = freq.get(arr[i], 0) + 1 
    return cnt


# Examples
print(countPairsWithDiffK([1, 4, 1, 4, 5], 3))  # Output: 4
print(countPairsWithDiffK([8, 16, 12, 16, 4, 0], 4))  # Output: 5

'''
Approach:
The idea is to count the frequency of each number in a hash map or dictionary as we go through the array Iterate over the array and for each element arr[i], 
we need another element say complement such that abs(arr[i] - complement) = k. Now, we can have two cases:

    (arr[i] - complement) is positive:
        arr[i] - complement = k
        So, complement = arr[i] - k
    (arr[i] - complement) is negative:
        (arr[i] - complement) = -k
        So, complement = arr[i] + k

So for each element arr[i], we can check if complement (arr[i] + k) or (arr[i] - k) is present in the hash map. 
If it is, increment the count variable by the occurrences of complement in map.

Complexity Analysis:

    Time Complexity: O(n)
        Building the frequency map takes O(n).
        Iterating over the map keys takes O(n) in the worst case.
    Space Complexity: O(n)
        The frequency map stores up to nn unique elements.
'''