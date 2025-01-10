'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/pair-with-given-sum-in-a-sorted-array4940

You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes. 

Examples :

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 3 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.

Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.

Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 125.

Constraints:
-105 <= target <=105
 2 <= arr.size() <= 105
-105 <= arr[i] <= 105
'''
def count_pairs_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    count = 0
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            # If elements at left and right are the same
            if arr[left] == arr[right]:
                n = right - left + 1
                count += n * (n - 1) // 2
                break  # No more pairs to process
            else:
                # Count duplicates at left
                left_count, right_count = 1, 1
                
                while left + 1 < right and arr[left] == arr[left + 1]:
                    left_count += 1
                    left += 1
                
                while right - 1 > left and arr[right] == arr[right - 1]:
                    right_count += 1
                    right -= 1
                
                # Add the product of counts to result
                count += left_count * right_count
                
                # Move both pointers
                left += 1
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return count

# Example usage
arr1 = [-1, 1, 5, 5, 7]
target1 = 6
print(count_pairs_with_sum(arr1, target1))  # Output: 3

arr2 = [1, 1, 1, 1]
target2 = 2
print(count_pairs_with_sum(arr2, target2))  # Output: 6

arr3 = [-1, 10, 10, 12, 15]
target3 = 125
print(count_pairs_with_sum(arr3, target3))  # Output: 0


'''
Algorithm

    Two-Pointer Approach
        Use two pointers: left (starting at the beginning of the array) and right (starting at the end).
        Compute the sum of the elements at left and right:
            If the sum equals target:
                Count all valid pairs that can be formed with the current elements (accounting for duplicates).
                Move both pointers inward.
            If the sum is less than target, move the left pointer to the right.
            If the sum is greater than target, move the right pointer to the left.

    Handling Duplicates
        If duplicates are present, count the occurrences of each element on both left and right sides to compute the total number of pairs efficiently.

    Edge Cases
        If the array has fewer than two elements, no pairs exist.
        If all numbers in the array are the same, ensure pairs are computed correctly.
        Ensure pairs do not involve the same index.

Complexity Analysis

    Time Complexity:
        Traversal of the array using two pointers: O(n).
        Counting duplicates for the current element pair: O(1) amortized (only done when duplicates exist).
        Overall: O(n).

    Space Complexity:
        No additional space is used apart from variables: O(1).

'''
