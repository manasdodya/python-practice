'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-bonus-problems/problem/pair-sum-in-a-sorted-and-rotated-array

Given an array of positive elements arr[] that is sorted and then rotated around an unknown point, the task is to check if the array has a pair with sum equals to a given target.

Examples:

Input: arr[] = [7, 9, 1, 3, 5], target = 6
Output: true
Explanation: arr[2] and arr[4] has sum equals to 6 which is equal to the target.

Input: arr[] = [2, 3, 4, 1], target = 3
Output: true
Explanation: arr[0] and arr[3] has sum equals to 3 which is equal to the target.

Input: arr[] = [10, 7, 4, 1], target = 9
Output: false
Explanation: There is no such pair exists in arr[] which sums to target.

Constraints:
2 <= arr.size() <=106
1 <= arr[i] <= 106
1 <= target <= 106
'''

def pairInSortedRotated(arr, target):
        #Your code here
        
        n = len(arr)
        
        if n < 2 :
            return False
        
        i = 0
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                break
            
        if arr[i] <= arr[i+1]:
            i += 1
        
        l = (i + 1) % n
        r = i
        
        while l != r:
            curr_sum = arr[l] + arr[r]
            
            if curr_sum == target:
                return True
            
            elif curr_sum < target:
                l = (l + 1) % n
                
            else:
                r = (r - 1 + n) % n
                
        return False

print(pairInSortedRotated([7, 9, 1, 3, 5], 6))  # True
print(pairInSortedRotated([2, 3, 4, 1], 3))  # True
print(pairInSortedRotated([10, 7, 4, 1], 9))  # False
print(pairInSortedRotated([5, 6, 1, 2, 3, 4], 9))  # True
print(pairInSortedRotated([1, 2, 3, 4, 5, 6], 11))  # True
print(pairInSortedRotated([1, 2, 3, 4, 5, 6], 20))  # False
print(pairInSortedRotated([3, 3, 3, 3, 3, 1, 2, 3, 3], 3)) # True

'''
Algorithm
    First find the largest element in an array which is the pivot point. The element just after the largest element is the smallest element. Once we have the indices of the largest and the smallest elements, we use two pointer technique to find the pair.

        Set the left pointer(l) to the smallest value and the right pointer(r) to the highest value.
        To handle the circular nature of the rotated array, we will use the modulo operation with the array size.
        While l ! = r, we shall keep checking if arr[l] + arr[r] = target.
            If arr[l] + arr[r] > target, update r = (r - 1 + n) % n.
            If arr[l] + arr[r] < target, update l = (l + 1) % n.
            If arr[l] + arr[r] = target, then return true.
        If no such pair is found after the iteration is complete, return false.

Time Complexity: O(n)
Space Complexity: O(1)
'''