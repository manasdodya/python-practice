'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/container-with-most-water0535

Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

Note: In the case of a single vertical line it will not be able to hold water.

Examples:

Input: arr[] = [1, 5, 4, 3]
Output: 6
Explanation: 5 and 3 are 2 distance apart. So the size of the base is 2. Height of container = min(5, 3) = 3. So, total area to hold water = 3 * 2 = 6.

Input: arr[] = [3, 1, 2, 4, 5]
Output: 12
Explanation: 5 and 3 are 4 distance apart. So the size of the base is 4. Height of container = min(5, 3) = 3. So, total area to hold water = 4 * 3 = 12.

Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25 
Explanation: 8 and 5 are 5 distance apart. So the size of the base is 5. Height of container = min(8, 5) = 5. So, the total area to hold water = 5 * 5 = 25.

Constraints:
1<= arr.size() <=105
1<= arr[i] <=104
'''

def max_water_area(arr):
    n = len(arr)
    if n < 2:
        return 0  # No water can be held with less than 2 lines
    
    left, right = 0, n - 1
    max_area = 0

    while left < right:
        # Calculate area
        height = min(arr[left], arr[right])
        width = right - left
        area = height * width

        # Update max_area if needed
        max_area = max(max_area, area)

        # Move the pointers
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example Usage
arr1 = [1, 5, 4, 3]
arr2 = [3, 1, 2, 4, 5]
arr3 = [2, 1, 8, 6, 4, 6, 5, 5]

print("Output for arr1:", max_water_area(arr1))  # Output: 6
print("Output for arr2:", max_water_area(arr2))  # Output: 12
print("Output for arr3:", max_water_area(arr3))  # Output: 25

'''
Algorithm: Two-Pointer Technique

    Initialize Pointers:
        Use two pointers: left starting at the beginning of the array and right starting at the end.
        Initialize max_area to store the maximum water area found so far.

    Calculate the Area:
        At each step, calculate the water area as:
        area=(right−left) × min⁡(arr[left],arr[right])
        Update max_area if the calculated area is larger than the current max_area.

    Move the Pointers:
        Move the pointer corresponding to the smaller height inward:
            If arr[left] < arr[right], increment left.
            Otherwise, decrement right.

    Stop When Pointers Meet:
        Continue until left and right pointers meet.

    Return Result:
        Return max_area.

Example Walkthrough
Input: arr = [1, 5, 4, 3]

    Initialization:
        left = 0, right = 3, max_area = 0.

    Step-by-Step:
        Calculate area: min(1, 3) * (3 - 0) = 1 * 3 = 3. Update max_area = 3.
        Move left since arr[left] < arr[right]: left = 1.
        Calculate area: min(5, 3) * (3 - 1) = 3 * 2 = 6. Update max_area = 6.
        Move right since arr[left] >= arr[right]: right = 2.
        Calculate area: min(5, 4) * (2 - 1) = 4 * 1 = 4. max_area remains 6.
        Move right: right = 1.
        Stop as left >= right.

Output: 6
Complexity Analysis

    Time Complexity:
        The algorithm performs a single traversal of the array: O(n), where n is the size of the array.

    Space Complexity:
        No extra space is used apart from variables: O(1).

Edge Cases

    Single Element:
        Input: arr = [5].
        Output: 0.

    All Elements Same:
        Input: arr = [3, 3, 3, 3].
        Output: 9.

    Decreasing or Increasing Heights:
        Input: arr = [5, 4, 3, 2] or arr = [1, 2, 3, 4].
        Output: Area between the first and last lines.

    Large Input:
        Efficient for 1≤n≤1051≤n≤105.
'''