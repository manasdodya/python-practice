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