'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/trapping-rain-water-1587115621

Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Examples:

Input: arr[] = [3, 0, 1, 0, 4, 0 2]
Output: 10
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides.

Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.

Constraints:
1 < arr.size() < 105
0 < arr[i] < 103
'''
def trap_water(arr):
    n = len(arr)
    if n < 3:
        return 0  # No water can be trapped if array has less than 3 blocks

    left, right = 0, n - 1
    left_max, right_max = 0, 0
    total_water = 0

    while left < right:
        if arr[left] <= arr[right]:
            if arr[left] < left_max:
                total_water += left_max - arr[left]
            else:
                left_max = arr[left]
            left += 1
        else:
            if arr[right] < right_max:
                total_water += right_max - arr[right]
            else:
                right_max = arr[right]
            right -= 1

    return total_water

# Example Usage
arr1 = [3, 0, 1, 0, 4, 0, 2]
arr2 = [3, 0, 2, 0, 4]
arr3 = [1, 2, 3, 4]
arr4 = [2, 1, 5, 3, 1, 0, 4]

print("Output for arr1:", trap_water(arr1))  # Output: 10
print("Output for arr2:", trap_water(arr2))  # Output: 7
print("Output for arr3:", trap_water(arr3))  # Output: 0
print("Output for arr4:", trap_water(arr4))  # Output: 9

'''
Algorithm: Two-Pointer Technique

    Initialize Two Pointers:
        Use two pointers, left (starting from the beginning) and right (starting from the end), to traverse the array.
        Maintain two variables, left_max and right_max, to store the maximum heights encountered so far from the left and right sides, respectively.

    Traverse the Array:
        While left < right, compare arr[left] and arr[right]:
            If arr[left] <= arr[right]:
                If arr[left] < left_max, calculate water trapped at left as left_max - arr[left]. Otherwise, update left_max.
                Move left pointer to the right.
            If arr[right] < arr[left]:
                If arr[right] < right_max, calculate water trapped at right as right_max - arr[right]. Otherwise, update right_max.
                Move right pointer to the left.

    Return Total Water:
        Sum up all water trapped at each step and return the result.

Example Walkthrough
Input: arr = [3, 0, 2, 0, 4]

    Initialize:
        left = 0, right = 4, left_max = 0, right_max = 0, total_water = 0.

    Step-by-Step:
        Compare arr[left] (3) and arr[right] (4). Update left_max = 3. Move left to 1.
        Compare arr[left] (0) and arr[right] (4). Add 3 - 0 = 3 to total_water. Move left to 2.
        Compare arr[left] (2) and arr[right] (4). Update left_max = 3. Add 3 - 2 = 1 to total_water. Move left to 3.
        Compare arr[left] (0) and arr[right] (4). Add 3 - 0 = 3 to total_water. Move left to 4.
        End traversal: total_water = 7.

Output: 7
Complexity Analysis

    Time Complexity:
        Single traversal of the array using two pointers: O(n).
        Total: O(n), where n is the size of the array.

    Space Complexity:
        No extra space used apart from variables: O(1).

Edge Cases

    No Blocks:
        Input: arr = [] or arr = [1].
        Output: 0.

    All Blocks of Same Height:
        Input: arr = [3, 3, 3, 3].
        Output: 0.

    Decreasing or Increasing Heights:
        Input: arr = [4, 3, 2, 1] or arr = [1, 2, 3, 4].
        Output: 0.

    Large Input:
        Efficient for 1≤n≤1051≤n≤105.

'''
