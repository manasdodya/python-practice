'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/count-pairs-with-given-sum--150253

Given an array arr[] and an integer target. You have to find numbers of pairs in array arr[] which sums up to given target.

Examples:

Input: arr[] = [1, 5, 7, -1, 5], target = 6 
Output: 3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) and (1, 5). 

Input: arr[] = [1, 1, 1, 1], target = 2 
Output: 6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

Input: arr[] = [10, 12, 10, 15, -1], target = 125
Output: 0

Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
1 <= target <= 104
'''

def countPairsWithSum(arr, target):
    freq = {}
    count = 0

    for num in arr:
        complement = target - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1

    return count

# Examples
arr1 = [1, 5, 7, -1, 5]
target1 = 6
print(countPairsWithSum(arr1, target1))  # Output: 3

arr2 = [1, 1, 1, 1]
target2 = 2
print(countPairsWithSum(arr2, target2))  # Output: 6

arr3 = [10, 12, 10, 15, -1]
target3 = 125
print(countPairsWithSum(arr3, target3))  # Output: 0


'''
Approach:

    Hash Map for Frequency:
        Use a hash map (freq) to store the frequency of elements we've seen so far.
        For each element xx, calculate its complement complement=target-xcomplement=target-x.
        If the complement exists in the hash map, the count of that complement gives the number of pairs formed with xx.

    Increment the Frequency:
        After processing xx, add it to the hash map or increment its frequency if it's already present.

    Edge Cases:
        If the array has fewer than 2 elements, return 0 (no pairs can be formed).

Algorithm:

    Initialize a variable count to store the number of pairs.
    Create an empty hash map freq to store the frequency of numbers.
    Iterate through the array:
        For each element xx, check if target-xtarget-x is in freq:
            If yes, add the frequency of target-xtarget-x to count.
        Increment the frequency of xx in freq.
    Return count.


Complexity:

    Time Complexity:
        Each element is processed once, and hash map operations (get/set) are O(1) on average.
        Overall: O(n), where n is the size of the array.

    Space Complexity:
        The hash map can store up to nn unique elements in the worst case.
        Overall: O(n).

Explanation of Examples:
Example 1:

Input: arr=[1,5,7,-1,5],target=6arr=[1,5,7,-1,5],target=6

    Complement pairs:
        11 → Complement 6-1=56-1=5: Found after processing 55.
        77 → Complement 6-7=-16-7=-1: Found after processing -1-1.
        Second 55 → Complement 6-5=16-5=1: Found after processing 11.
    Total pairs: 3.

Example 2:

Input: arr=[1,1,1,1],target=2arr=[1,1,1,1],target=2

    All pairs of 11 sum to 22: 6 combinations in total.

Example 3:

Input: arr=[10,12,10,15,-1],target=125arr=[10,12,10,15,-1],target=125

    No pairs add up to 125125. Output: 00.

This approach handles duplicates efficiently and works well within the given constraints.

'''