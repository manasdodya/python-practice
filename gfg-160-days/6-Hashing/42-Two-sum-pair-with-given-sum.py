'''
URL - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/key-pair5616

Given an array arr[] of positive integers and another integer target. Determine if there exists two distinct indices such that the sum of there elements is equals to target.

Examples:

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 16
Output: true
Explanation: arr[3] + arr[4] = 6 + 10 = 16.

Input: arr[] = [1, 2, 4, 3, 6], target = 11
Output: false
Explanation: None of the pair makes a sum of 11.

Input: arr[] = [11], target = 11
Output: false
Explanation: No pair is possible as only one element is present in arr[].

Constraints:
1 ≤ arr.size ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ target ≤ 2*105
'''
def hasPairWithSum(arr, target):
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False

# Examples
arr1 = [1, 4, 45, 6, 10, 8]
target1 = 16
print(hasPairWithSum(arr1, target1))  # Output: true

arr2 = [1, 2, 4, 3, 6]
target2 = 11
print(hasPairWithSum(arr2, target2))  # Output: false

arr3 = [11]
target3 = 11
print(hasPairWithSum(arr3, target3))  # Output: false

'''
Approach:

    Use a Hash Set:
        Iterate through the array and keep track of the elements you've seen so far in a hash set.
        For each element xx in the array, calculate the required complement complement=target-x
        Check if the complement exists in the hash set:
            If yes, return true (a pair exists).
            If no, add the current element xx to the hash set and continue.

    Early Exit:
        The moment you find a valid pair, you can stop further computation, making this approach efficient.

    Edge Cases:
        If the array size is less than 2, return false (no pairs are possible).

To determine if there exist two distinct indices such that the sum of their elements equals the target, we can use an efficient approach based on hashing. Here's the solution:
Approach:

    Use a Hash Set:
        Iterate through the array and keep track of the elements you've seen so far in a hash set.
        For each element xx in the array, calculate the required complement complement=target-xcomplement=target-x.
        Check if the complement exists in the hash set:
            If yes, return true (a pair exists).
            If no, add the current element xx to the hash set and continue.

    Early Exit:
        The moment you find a valid pair, you can stop further computation, making this approach efficient.

    Edge Cases:
        If the array size is less than 2, return false (no pairs are possible).

Complexity:

    Time Complexity:
        Each element is processed once, and lookups/additions in a hash set are O(1) on average.
        Overall: O(n), where n is the size of the array.

    Space Complexity:
        The hash set requires O(n) space in the worst case.

Explanation of Examples:
Input:

arr = [1, 4, 45, 6, 10, 8], target = 16

    Process 11: Complement = 16-1=15. Add 1 to the set. Set: {1}.
    Process 44: Complement = 16-4=12. Add 4 to the set. Set: {1,4}.
    Process 4545: Complement = 16-45=-29. Add 45 to the set. Set: {1,4,45}.
    Process 66: Complement = 16-6=10. Add 6 to the set. Set: {1,4,45,6}.
    Process 1010: Complement = 16-10=6. 6 is in the set. Return true.

'''