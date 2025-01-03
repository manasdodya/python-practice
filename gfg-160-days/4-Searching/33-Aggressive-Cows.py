'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/aggressive-cows

You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

Examples :

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.

Input: stalls[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows, in this case, is 4, which also is the largest among all possible ways.

Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
Output: 1
Explanation: Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the number of cows.
The minimum distance between cows, in this case, is 1, which also is the largest among all possible ways.

Constraints:
2 <= stalls.size() <= 106
0 <= stalls[i] <= 108
1 <= k <= stalls.size()
'''

def canPlaceCows(stalls, k, min_distance):
    count = 1  # Place the first cow in the first stall
    last_position = stalls[0]
    
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_distance:
            count += 1
            last_position = stalls[i]
            if count == k:
                return True
    return False

def aggressiveCows(stalls, k):
    # Sort stalls to consider distances in sorted order
    stalls.sort()
    
    # Binary search on the answer
    low, high = 1, stalls[-1] - stalls[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if canPlaceCows(stalls, k, mid):
            result = mid  # Update the result
            low = mid + 1  # Try for a larger minimum distance
        else:
            high = mid - 1  # Reduce the maximum distance
    
    return result

# Test examples
examples = [
    ([1, 2, 4, 8, 9], 3),
    ([10, 1, 2, 7, 5], 3),
    ([2, 12, 11, 3, 26, 7], 5)
]

for i, (stalls, k) in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: stalls={stalls}, k={k}")
    print(f"  Output: {aggressiveCows(stalls, k)}")
    print()

'''
Approach

    Sort the Stalls:
        Since we need to calculate distances between stalls, sort the array to facilitate placement of cows.

    Binary Search on Distance:
        Use binary search to find the maximum possible minimum distance.
        Let low be 1 (minimum possible distance) and high be the difference between the maximum and minimum positions in the sorted stalls.

    Check Feasibility:
        Use a helper function to check if it is possible to place kk cows with at least a given minimum distance.
        Place the first cow in the first stall and iterate through the rest to place other cows, ensuring the distance condition is met.

    Update Search Space:
        If placement is possible, increase the lower bound (low) to try larger distances.
        If not, decrease the upper bound (high).

    Output the Result:
        The largest valid low value is the answer.


Explanation of Example
Input: stalls = [1, 2, 4, 8, 9], k = 3

    Sorting: Stalls become [1, 2, 4, 8, 9].
    Binary Search:
        Start with low = 1 and high = 8.
        Middle distance mid = (1 + 8) // 2 = 4.
        Check feasibility:
            Place the first cow at stalls[0] = 1.
            Place the second cow at stalls[3] = 8 (distance = 7).
            Placement fails for the third cow.
        Decrease high to 3.
        Repeat until low > high.
    Result: The maximum minimum distance is 3.

Complexity Analysis

    Time Complexity:
        Sorting: O(nlogn)
        Binary search: O(log(max_distance)).
        Feasibility check: O(n).
        Overall: O(nlogn+nlog(max_distance)), where max_distance=max(stalls) - min(stalls).

    Space Complexity:
        O(1) additional space (in-place operations).
'''