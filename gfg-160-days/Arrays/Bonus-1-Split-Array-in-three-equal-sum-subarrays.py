'''
URL - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/array-bonus-problems/problem/split-array-in-three-equal-sum-subarrays

Given an array, arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. If possible, return any index pair(i, j) in an array such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise return an array {-1,-1}.

Note: Since multiple answers are possible, return any of them. The driver code will print true if it is correct otherwise, it will print false.

Examples :

Input:  arr[] = [1, 3, 4, 0, 4]
Output: true
Explanation: [1, 2] is valid pair as sum of subarray arr[0..1] is equal to sum of subarray arr[2..3] and also to sum of subarray arr[4..4]. The sum is 4, so driver code prints true.

Input: arr[] = [2, 3, 4]
Output: false
Explanation: No three subarrays exist which have equal sum.

Input: arr[] = [0, 1, 1]
Output: false

Constraints:
3 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106

'''

def findSplit(arr):
    total = sum(arr)
    
    if total % 3 != 0:
        return [-1, -1]
    
    target_sum = total // 3
    cumulative_sum = 0
    first_split = -1
    second_split = -1
    
    for i in range(len(arr)):
        cumulative_sum += arr[i]
        
        if cumulative_sum == target_sum and first_split == -1:
            first_split = i
        elif cumulative_sum == 2 * target_sum and first_split != -1:
            second_split = i
            break  # No need to continue further

    if first_split != -1 and second_split != -1 and second_split < len(arr) - 1:
        return [first_split, second_split]
    
    return [-1, -1]

# Example Usage
print(findSplit([1, 3, 4, 0, 4]))  # Output: [1, 2]
print(findSplit([2, 3, 4]))        # Output: [-1, -1]
print(findSplit([1, -1, 1, -1, 1, -1, 1, -1]))  # Output: [1, 3]

'''
Algorithm:

    Calculate the Total Sum:

        If the total sum is not divisible by 3, return [-1, -1].

    Iterate Through the Array:

        Use a variable to track the cumulative sum while traversing the array.
        Find the first index i where the cumulative sum equals the first target sum (total_sum // 3).
        Continue and find the next index j where the cumulative sum equals twice the target sum (2 * total_sum // 3).

    Return Indices:

        Ensure j is not the last index to guarantee three non-empty parts.
        If indices i and j are valid, return [i, j].
        Otherwise, return [-1, -1]

Explanation:

    Tracking Split Points:
        first_split is recorded when the cumulative sum equals target_sum.
        second_split is recorded when the cumulative sum equals 2 * target_sum.

    Stopping Early:
        The loop exits as soon as both split points are identified.

    Validation:
        Ensure second_split is not at the last index to leave a non-empty third segment.

Complexity:

    Time Complexity: O(n)O(n), as we traverse the array once.
    Space Complexity: O(1)O(1), as we use only a few variables.

Example Outputs:

    Input: [1, 3, 4, 0, 4]
        Total sum = 12, target sum = 4.
        First split at index 1, second split at index 2.
        Output: [1, 2].

    Input: [2, 3, 4]
        Total sum = 9, target sum = 3.
        No valid splits. Output: [-1, -1].

    Input: [1, -1, 1, -1, 1, -1, 1, -1]
        Total sum = 0, target sum = 0.
        First split at index 1, second split at index 3.
        Output: [1, 3].
'''