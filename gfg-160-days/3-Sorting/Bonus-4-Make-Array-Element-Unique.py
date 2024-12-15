'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-bonus-problems/problem/make-array-elements-unique--170645

Given an integer array arr[ ], your task is to find the minimum number of increment operations required to make all the array elements unique. i.e. no value in the array should occur more than once. In one operation, a value can be incremented by 1 only.

Note: The answer will always fit into a 32-bit integer.

Examples :

Input: arr[] = [3, 2, 1, 2, 1, 7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7]. It can be shown that it is impossible for the array to have all unique values with 5 or less operations.

Input: arr[] = [1, 2, 2]
Output: 1
Explanation: After one operation [2 -> 3], the array could be [1, 2, 3].

Input: arr[] = [5, 4, 3, 2, 1]
Output: 0
Explanation: All elements are unique.

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106
'''

def minIncrementForUnique(arr):
    # Sort the array
    arr.sort()

    # Variable to store the number of moves
    moves = 0

    # Iterate through the array
    for i in range(1, len(arr)):
        # If current element is not unique
        if arr[i] <= arr[i - 1]:
            # Calculate the needed increment
            increment = arr[i - 1] - arr[i] + 1
            # Apply the increment
            arr[i] += increment
            # Add the increment to the moves
            moves += increment

    return moves

# Test examples
examples = [
    [3, 2, 1, 2, 1, 7],
    [1, 2, 2],
    [5, 4, 3, 2, 1]
]

for i, arr in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: {arr}")
    print(f"  Output: {minIncrementForUnique(arr)}")
    print()

'''
Algorithm

    Sort the Array:
        Sort the array in ascending order to handle duplicates more systematically.

    Iterate Through the Array:
        Traverse the array and check if the current element is less than or equal to the previous element.
        If so, increment the current element to one more than the previous element. Keep a count of the number of increments made.

    Return the Count:
        The total number of increments needed to make the array unique is the answer.

Example Walkthrough
Example 1: arr = [3, 2, 1, 2, 1, 7]

    Sort the array: [1, 1, 2, 2, 3, 7]
    Start iterating:
        For index 1: 1 (duplicate of previous 1). Increment to 2. Moves = 1.
        For index 2: 2 (duplicate of previous 2). Increment to 3. Moves = 2.
        For index 3: 2 becomes 3. Increment to 4. Moves = 3.
        For index 4: 3 becomes 4. Increment to 5. Moves = 4.
        For index 5: Already 7 (unique). No increment needed.
    Final Array: [1, 2, 3, 4, 5, 7]
    Total Moves: 6

Output: 6

Time Complexity:

    Sorting: O(nlogn)
    Iteration and Increment Calculation: O(n)O(n)

Overall: O(nlogn)
Space Complexity:

    Sorting uses O(1) (in-place sorting for the array).
    No additional data structures are used.
'''