'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/prefix-sum-bonus-problem/problem/number-of-times-graph-cuts-x-axis

Given an integer array arr[], where each arr[i] denotes the trajectory of the graph over the plane; i.e. arr[i]>0 means graph going above its current position by arr[i] value and arr[i]<0 means graph going down by arr[i] value. If initial position of the graph is at origin, determines the number of times graph crosses or touches the X-axis.

Example:

Input: arr[] = [2, 5, -9, 4]
Output: 2
Explanation: Graph touches the X-axis two times through index 1 to 2, and through index 2 to 3.

Input: arr[] = [4, -6, 2, 8, -2, 3, -12]
Output: 3
Explanation:

Graph touches the X-axis three times through index 0 to 1, through index 1 to 2, and through index 5 to 6.

Input: arr[] = [1, 3, 5]
Output: 0
Explanation: Graph has not touched the X-axis any time.

Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
arr[i] does not contains any zero.
'''

def count_x_axis_crossings(arr):
    position = 0  # Starting at the origin
    crossings = 0  # Count of X-axis crossings
    prev_position = 0  # Tracks the previous position
    
    for num in arr:
        prev_position = position  # Store the previous position
        position += num  # Update the current position
        
        # If previous position was above/below 0 and now it's the opposite side or exactly 0
        if (prev_position > 0 and position <= 0) or (prev_position < 0 and position >= 0):
            crossings += 1  # X-axis crossed or touched

    return crossings

# Example test cases
print(count_x_axis_crossings([2, 5, -9, 4]))  # Output: 2
print(count_x_axis_crossings([4, -6, 2, 8, -2, 3, -12]))  # Output: 3
print(count_x_axis_crossings([1, 3, 5]))  # Output: 0

'''
Algorithm Explanation:

    Understanding the movement:
        Each element in arr[] represents a vertical movement.
        If arr[i] > 0, the graph moves up.
        If arr[i] < 0, the graph moves down.

    Tracking the position:
        We start at position 0 (origin).
        Maintain a variable position to track the current height of the graph.

    Detecting X-axis crosses/touches:
        Whenever position becomes 0, the graph touches the X-axis.
        If position moves from positive to negative or negative to positive, it means the graph has crossed the X-axis.

    Implementation Approach:
        Initialize position = 0.
        Iterate through arr[] and update position.
        Check if position crosses or touches 0 and count such occurrences.

Example Walkthrough:
Example 1:

Input: [2, 5, -9, 4]
Tracking position changes:

    0 → 2 → 7 → -2 (crosses X-axis) → 2
    The graph crosses/touches X-axis 2 times.

Output: 2
Example 2:

Input: [4, -6, 2, 8, -2, 3, -12]
Tracking position changes:

    0 → 4 → -2 (crosses X-axis) → 0 (touches X-axis) → 8 → 6 → 9 → -3 (crosses X-axis)
    The graph crosses/touches X-axis 3 times.

Output: 3
Complexity Analysis:

    Time Complexity: O(N) → We traverse the array once.
    Space Complexity: O(1) → Only a few extra variables are used.
        
'''