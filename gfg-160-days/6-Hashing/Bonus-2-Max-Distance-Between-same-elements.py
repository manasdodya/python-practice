'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-bonus-problem/problem/max-distance-between-same-elements

Given an array arr[], the task is to find the maximum distance between two occurrences of an element. If no element has two occurrences, then return 0.

Examples:

Input: arr[] = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.

Input: arr[] = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation: maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 10-5 = 5, So max distance is 10.

Input: arr[] = [1, 2, 3, 6, 5, 4]
Output: 0
Explanation: No element has two occurrences, so maximum distance = 0.

Expected Time Complexity :  O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 109  

'''
def maxDistance(arr):
    first_occurrence = {}
    max_dist = 0
    
    for i, value in enumerate(arr):
        if value in first_occurrence:
            # Calculate the distance between the current and first occurrence
            max_dist = max(max_dist, i - first_occurrence[value])
        else:
            # Store the first occurrence index
            first_occurrence[value] = i
    
    return max_dist

# Examples
print(maxDistance([1, 1, 2, 2, 2, 1]))  # Output: 5
print(maxDistance([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]))  # Output: 10
print(maxDistance([1, 2, 3, 6, 5, 4]))  # Output: 0

'''
Approach

    Use a dictionary to store the first occurrence of each element.
    Iterate through the array:
        If the element is seen for the first time, store its index in the dictionary.
        If the element is already in the dictionary, calculate the distance between the current index and the stored index.
    Update the maximum distance whenever a larger value is found.
    If no element has two occurrences, return 0.

Explanation
Example 1:

Input: arr = [1, 1, 2, 2, 2, 1]

    First occurrence dictionary: {1: 0, 2: 2}
    Distances:
        1: 5-0=5
        2: 4-2=2
    Maximum distance: max(5,2)=5

Example 2:

Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]

    First occurrence dictionary: {3: 0, 2: 1, 1: 2, 4: 5, 5: 6, 8: 7, 6: 8, 7: 9}
    Distances:
        2: 11-1=10
        1: 4-2=2
        4: 10-5=5
    Maximum distance: =10

Example 3:

Input: arr = [1, 2, 3, 6, 5, 4]

    No repeated elements.
    Maximum distance: 0.

Complexity Analysis

    Time Complexity: O(n)
        We traverse the array once and perform constant-time operations for each element.
    Space Complexity: O(n)
        The dictionary stores at most nn unique elements.

'''