'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/array-bonus-problems/problem/maximize-number-of-1s0905

Given a binary array arr[] (containing only 0s and 1s) and an integer k, you are allowed to flip at most k 0s to 1s. Find the maximum number of consecutive 1's that can be obtained in the array after performing the operation at most k times.

Examples:

Input: arr[] = [1, 0, 1], k = 1
Output: 3
Explanation: Maximum subarray of consecutive 1's is of size 3 which can be obtained after flipping the zero present at the 1st index.

Input: arr[] = [1, 0, 0, 1, 0, 1, 0, 1], k = 2
Output: 5
Explanation: By flipping the zeroes at indices 4 and 6, we get the longest subarray from index 3 to 7 containing all 1’s.

Input: arr[] = [1, 1], k = 2
Output: 2
Explanation: Since the array is already having the max consecutive 1's, hence we dont need to perform any operation. Hence the answer is 2

Constraints:
1 <= arr.size() <= 105
0 <= k <= arr.size()
0 <= arr[i] <= 1

'''

def longestSubarray(arr, k):
    start = 0  # Start of the sliding window
    max_len = 0  # To track the maximum length of subarray
    zero_count = 0  # To track the number of 0s in the current window
    
    # Iterate through the array with the 'end' pointer
    for end in range(len(arr)):
        if arr[end] == 0:
            zero_count += 1
        
        # If there are more than k zeros, shrink the window from the left
        while zero_count > k:
            if arr[start] == 0:
                zero_count -= 1
            start += 1
        
        # Update the maximum length of the subarray
        max_len = max(max_len, end - start + 1)
    
    return max_len


arr = [1,0,1]
k = 1
print(longestSubarray(arr,k)) # output = 3

arr = [1, 0, 0, 1, 0, 1, 0, 1]
k = 2
print(longestSubarray(arr,k)) # output = 5

arr = [1,1]
k = 2
print(longestSubarray(arr, k)) #output = 2

'''
Problem Breakdown:

    Sliding Window Concept:
        We maintain a sliding window [start, end] where start and end represent the boundaries of the subarray.
        We expand the window by moving the end pointer to the right and count the number of zeros within the window.
        If the number of zeros exceeds k, we shrink the window by moving the start pointer to the right until the number of zeros is less than or equal to k.

    Key Idea:
        As long as the number of zeros in the window is less than or equal to k, we can keep expanding the window and keep track of the length of the current subarray.
        If the number of zeros exceeds k, we move the start pointer rightwards until the number of zeros in the window becomes k or fewer again.

    Time Complexity:
        Each element is processed at most twice, once when end expands the window and once when start shrinks the window. This gives a time complexity of O(n), where n is the size of the array.

    Space Complexity:
        Since we are only using a few variables (pointers and counters), the space complexity is O(1).
    
Explanation of the Code:

    start and end: These represent the sliding window's two pointers. start is the left boundary, and end is the right boundary of the window.
    zero_count: This variable keeps track of the number of zeros in the current window. If zero_count exceeds k, the window is adjusted by moving the start pointer to the right until the number of zeros is less than or equal to k.
    max_len: This variable keeps track of the maximum length of the subarray that can be obtained with at most k flips.

Time Complexity:

    The function processes each element of the array at most twice, once when expanding the window with end and once when shrinking the window with start. Hence, the time complexity is O(n), where n is the length of the array.

Space Complexity:

    We are using a constant amount of extra space (just a few integer variables). Hence, the space complexity is O(1).

Example Walkthrough:
Example 1:

Input: arr = [1, 0, 1], k = 1

    Step 1: Start with start = 0, end = 0, zero_count = 0, max_len = 0.
        arr[0] = 1: No change in zero_count. max_len = 1 (window: [1]).
    Step 2: Move end to 1.
        arr[1] = 0: Increment zero_count to 1. max_len = 2 (window: [1, 0]).
    Step 3: Move end to 2.
        arr[2] = 1: No change in zero_count. max_len = 3 (window: [1, 0, 1]).
    End: The maximum subarray length is 3.

Output: 3
Example 2:

Input: arr = [1, 0, 0, 1, 0, 1, 0, 1], k = 2

    Step 1: Start with start = 0, end = 0, zero_count = 0, max_len = 0.
        arr[0] = 1: No change in zero_count. max_len = 1 (window: [1]).
    Step 2: Move end to 1.
        arr[1] = 0: Increment zero_count to 1. max_len = 2 (window: [1, 0]).
    Step 3: Move end to 2.
        arr[2] = 0: Increment zero_count to 2. max_len = 3 (window: [1, 0, 0]).
    Step 4: Move end to 3.
        arr[3] = 1: No change in zero_count. max_len = 4 (window: [1, 0, 0, 1]).
    Step 5: Move end to 4.
        arr[4] = 0: Increment zero_count to 3. Now zero_count > k, so we move start to 1 (shrink window).
        max_len = 5 (window: [0, 0, 1, 0, 1]).
    End: The maximum subarray length is 5.

Output: 5

'''