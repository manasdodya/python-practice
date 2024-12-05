'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/minimize-the-heights3351

Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

    Increase the height of the tower by K
    Decrease the height of the tower by K

Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

Examples :

Input: k = 2, arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.

Input: k = 3, arr[] = {3, 9, 12, 16, 20}
Output: 11
Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11. 

Expected Time Complexity: O(n*logn)
Expected Auxiliary Space: O(n)

Constraints
1 ≤ k ≤ 107
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 107

'''
class Solution:
    def getMinDiff(self, arr, k):
        # Sort the array first
        arr.sort()
        
        # Number of elements
        n = len(arr)
        
        # If there's only one tower, no need to modify anything
        if n == 1:
            return 0
        
        # Initialize the result as the difference between max and min heights
        result = arr[n - 1] - arr[0]
        
        # Consider both increasing and decreasing each tower height
        for i in range(1, n):
            # We can only decrease if the new height is >= 0
            if arr[i] - k < 0:
                continue
            
            # Calculate the new minimum and maximum possible heights after modification
            minH = min(arr[0] + k, arr[i] - k)
            maxH = max(arr[i - 1] + k, arr[n - 1] - k)
            
            # Update the result with the minimal possible difference
            result = min(result, maxH - minH)
        
        return result

# Example usage
solution = Solution()

# Test case 1
arr = [1, 5, 8, 10]
k = 2
print(solution.getMinDiff(arr, k))  # Output: 5

# Test case 2
arr = [3, 9, 12, 16, 20]
k = 3
print(solution.getMinDiff(arr, k))  # Output: 11


'''
Problem Breakdown:

    For each tower height, we are allowed to either increase the height by kk or decrease the height by kk, with the constraint that no tower height can become negative.
    After modifying all the towers, we need to minimize the difference between the tallest and shortest tower.

Approach:

    Sort the Array:
        The key insight is that after sorting the tower heights, the possible modifications (increasing or decreasing) will cause the new heights to form two ranges:
            Increasing the smaller values and decreasing the larger values.
            This approach works because modifying the towers in this way helps bring the height values closer to each other.

    Two Possible Operations:
        For each tower, you can either:
            Increase the height by kk, or
            Decrease the height by kk.
        The idea is to perform operations in a way that the heights remain balanced. Specifically, we should be mindful of the smallest and largest heights in the sorted array and minimize the gap between them.

    Minimizing the Difference:
        After modifying the heights, the maximum and minimum values in the array will dictate the difference. To minimize the difference, we need to explore the effect of choosing the best modification for each tower.

    Optimization Strategy:
        After sorting the array, we evaluate the possible outcomes for the first and last tower.
        The minimal difference occurs when the highest tower is decreased and the smallest tower is increased, or some combination of both. After modifying the towers, calculate the difference between the maximum and minimum heights.

    Time Complexity:
        Sorting the array will take O(nlogn), and the subsequent checks will be O(n), so the overall time complexity is O(nlogn).

Example Walkthrough:

Let's walk through the example k = 2 and arr = [1, 5, 8, 10]:

    Sort the Array:

arr = [1, 5, 8, 10]

Initial Difference: The difference between the largest and smallest towers before any modification is:

    result = 10 - 1 = 9

    Modifying the Heights:
        We can increase or decrease each tower’s height by 2 (k = 2). Consider each tower and compute possible values.

    For example:
        For the tower with height 1, increase by 2 gives 3, and for the tower 5, decrease by 2 gives 3. This creates a more balanced distribution.

    After modifications, the array becomes {3, 3, 6, 8}, and the difference between the largest and smallest towers is 8 - 3 = 5.

Final Result:

Output: 5

Explanation of the Code:

    Sorting:
        We begin by sorting the array to make it easier to compare the smallest and largest heights and their differences.

    Initial Calculation:
        We compute the initial difference between the tallest and shortest towers.

    Iterating Over Towers:
        For each tower, we evaluate the effect of both increasing and decreasing the height and calculate the new possible difference. We continually track the smallest possible difference.

    Edge Case:
        If there is only one tower, no modification is possible, so the result is 0.

Time Complexity:

    Sorting the Array: O(nlogn)
    Iterating over the Array: O(n)
    Overall Complexity: O(nlogn)
'''