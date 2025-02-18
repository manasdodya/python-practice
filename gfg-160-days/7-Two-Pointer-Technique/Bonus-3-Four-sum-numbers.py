'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-bonus-problems/problem/find-all-four-sum-numbers1732

Given an array arr[] of integers and another integer target. Find all unique quadruples from the given array that sums up to target.

Note: All the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] it should be : q1 <= q2 <= q3 <= q4.

Examples :

Input: arr[] = [0, 0, 2, 1, 1], target = 3
Output: [0, 0, 1, 2] 
Explanation: Sum of 0, 0, 1, 2 is equal to 3.

Input: arr[] = [10, 2, 3, 4, 5, 7, 8], target = 23
Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]] 
Explanation: Sum of 2, 3, 8, 10 is 23, sum of 2, 4, 7, 10 is 23 and sum of 3, 5, 7, 8 is also 23.

Input: arr[] = [0, 0, 2, 1, 1], target = 2
Output: [0, 0, 1, 1] 
Explanation: Sum of 0, 0, 1, 1 is equal to 2.

Constraints:
1 <= arr.size() <= 200
-106 <= target <= 106
-106 <= arr[i] <= 106
'''

def fourSum(arr, target):
    arr.sort()  # Step 1: Sort the array
    n = len(arr)
    result = []

    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicate elements for the first index
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:  # Skip duplicate elements for the second index
                continue

            left, right = j + 1, n - 1  # Two pointers
            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if current_sum == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])
                    
                    # Move `left` forward, skipping duplicates
                    left += 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1

                    # Move `right` backward, skipping duplicates
                    right -= 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif current_sum < target:
                    left += 1  # Increase the sum
                else:
                    right -= 1  # Decrease the sum

    return result

# Example runs
arr1 = [0, 0, 2, 1, 1]
target1 = 3
print(fourSum(arr1, target1))  # Output: [[0, 0, 1, 2]]

arr2 = [10, 2, 3, 4, 5, 7, 8]
target2 = 23
print(fourSum(arr2, target2))  # Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]]

arr3 = [0, 0, 2, 1, 1]
target3 = 2
print(fourSum(arr3, target3))  # Output: [[0, 0, 1, 1]]


'''
Algorithm Explanation

The problem requires finding all unique quadruples (four elements) in an array that sum up to a given target. A brute-force approach using four nested loops would have a complexity of O(n4)O(n4), which is inefficient. Instead, we use a two-pointer technique combined with sorting to reduce the complexity.
Steps:

    Sort the array: Sorting helps efficiently navigate the elements and avoid duplicate quadruples.
    Fix two elements: Use two nested loops to fix the first (i) and second (j) elements.
    Two-pointer approach: Use two pointers (left and right) to find the remaining two elements that sum to target - (arr[i] + arr[j]).
    Avoid duplicates: Skip duplicate elements to ensure uniqueness in quadruples.
    Store unique quadruples: If a quadruple is found, add it to the result list.

Complexity Analysis

    Sorting the array: O(nlogn)
    Looping through the array: O(n2) for fixing two elements
    Two-pointer traversal: O(n) in the worst case
    Overall Complexity: O(n3), which is optimal for the given constraints (n≤200n≤200)

'''