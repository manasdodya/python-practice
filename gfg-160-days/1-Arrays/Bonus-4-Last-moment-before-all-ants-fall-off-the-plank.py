'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/array-bonus-problems/problem/last-moment-before-all-ants-fall-out-of-a-plank

We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second. Some of the ants move to the left, the other move to the right.
When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time. When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.

Given an integer n and two integer arrays left[] and right[], the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank.

Examples :

Input: n = 4, left[] = [2], right[] = [0, 1, 3]
Output: 4
        
Explanation: As seen in the above image, the last ant falls off the plank at t = 4.

Input:  n = 4, left[] = [], right[] = [0, 1, 2, 3, 4]
Output: 4
        
 Explanation: All ants are going to the right, the ant at index 0 needs 7 seconds to fall.

Input: n = 3, left[] = [0], right[] = [3]
Output: 0
Explanation: The ants will fall off the plank as they are already on the end of the plank.

Constraints:
1 <= n <= 105
0 <= left.length <= n + 1
0 <= left[i] <= n
0 <= right.length <= n + 1
0 <= right[i] <= n
1 <= left.length + right.length <= n + 1
All values of left and right are unique, and each value can appear only in one of the two arrays.
'''

# Python Code to find the last moment before all  
# ants fall off the plank

def getLastMoment(n, left, right):
    res = 0

    # Find the time to fall off the plank for all 
    # ants moving towards left
    for i in range(len(left)):
        res = max(res, left[i])

    # Find the time to fall off the plank for all 
    # ants moving towards right
    for i in range(len(right)):
        res = max(res, n - right[i])

    # Return the maximum time among all ants
    return res

n = 4
left = [2]
right = [0, 1, 3]
print(getLastMoment(n, left, right)) # output = 4

n = 7
left = []
right = [0, 1, 2, 3, 4]
print(getLastMoment(n, left, right))  # Output: 7

n = 3
left = [0]
right = [3]
print(getLastMoment(n, left, right))  # Output: 3


'''
The provided code correctly determines the last moment when all ants fall off the plank. Here's an explanation and analysis of your code:
How It Works:

    Inputs:
        nn: Length of the plank.
        left: List of positions of ants moving to the left.
        right: List of positions of ants moving to the right.

    Logic:
        For each ant moving to the left, it will fall off at t=positiont=position. The maximum of these times is the last moment for ants moving left.
        For each ant moving to the right, it will fall off at t=n-positiont=n-position. The maximum of these times is the last moment for ants moving right.
        The overall last moment is the maximum between these two computed values.

    Return Value:
        The maximum time among all the ants.

Example Execution:
Input:

    n=4n=4
    left = [2]
    right = [0, 1, 3]

Execution Steps:

    Initialize res = 0.
    Process left:
        res=max(0,2)=2res=max(0,2)=2.
    Process right:
        res=max(2,4-0)=4res=max(2,4-0)=4.
        res=max(4,4-1)=4res=max(4,4-1)=4.
        res=max(4,4-3)=4res=max(4,4-3)=4.
    Return res=4res=4.

Output:

4
Complexity Analysis:

    Time Complexity:
        Processing left takes O(m), where mm is the length of the left array.
        Processing right takes O(p), where pp is the length of the right array.
        Total: O(m+p)O(m+p).

    Space Complexity:
        The code uses O(1) extra space.
'''