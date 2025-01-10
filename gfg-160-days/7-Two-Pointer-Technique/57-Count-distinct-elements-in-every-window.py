'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/count-distinct-elements-in-every-window

Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]
Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.

Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: Window 1 of size k = 2 is 4 1. Number of distinct elements in this window are 2. 
Window 2 of size k = 2 is 1 1. Number of distinct elements in this window is 1. 

Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]

Constraints:
1 <= k <= arr.size() <= 105
1 <= arr[i] <= 105
'''

def count_distinct_in_window(arr, k):
    n = len(arr)
    if k > n:
        return []

    freq_map = {}
    result = []
    start = 0

    for end in range(n):
        # Add the current element to the frequency map
        freq_map[arr[end]] = freq_map.get(arr[end], 0) + 1

        # If window size exceeds k, shrink the window from the left
        if end - start + 1 > k:
            freq_map[arr[start]] -= 1
            if freq_map[arr[start]] == 0:
                del freq_map[arr[start]]
            start += 1

        # If we have a valid window, store the distinct count
        if end - start + 1 == k:
            result.append(len(freq_map))

    return result

# Example Usage
arr1 = [1, 2, 1, 3, 4, 2, 3]
k1 = 4
print("Output for arr1:", count_distinct_in_window(arr1, k1))  # Output: [3, 4, 4, 3]

arr2 = [4, 1, 1]
k2 = 2
print("Output for arr2:", count_distinct_in_window(arr2, k2))  # Output: [2, 1]

arr3 = [1, 1, 1, 1, 1]
k3 = 3
print("Output for arr3:", count_distinct_in_window(arr3, k3))  # Output: [1, 1, 1]


'''
Algorithm (Sliding Window + Two Pointers)

    Use a hash map freq_map to store the frequency of elements in the current window.
    Use two pointers:
        start: The beginning of the current window.
        end: The end of the current window.
    Process the array:
        Expand the window by moving end and adding the element at arr[end] to freq_map.
        If the window size exceeds k, shrink it by moving start and removing arr[start] from freq_map.
        Track the number of distinct elements using the size of freq_map.
    Store the count of distinct elements for each window.
    Return the results.

Example Walkthrough
Example 1:

Input:
arr = [1, 2, 1, 3, 4, 2, 3], k = 4

    First Window [1, 2, 1, 3]:
        Frequencies: {1: 2, 2: 1, 3: 1} → Distinct count = 3.

    Second Window [2, 1, 3, 4]:
        Remove 1, Add 4: {2: 1, 1: 1, 3: 1, 4: 1} → Distinct count = 4.

    Third Window [1, 3, 4, 2]:
        Remove 2, Add 2: {1: 1, 3: 1, 4: 1, 2: 1} → Distinct count = 4.

    Fourth Window [3, 4, 2, 3]:
        Remove 1, Add 3: {3: 2, 4: 1, 2: 1} → Distinct count = 3.

Output: [3, 4, 4, 3]

Complexity Analysis

    Time Complexity:
        Processing each element once in the sliding window: OO(n).
        Hash map operations (insert, delete, get): O(1) on average.
        Total: O(n).

    Space Complexity:
        Storing frequencies in the hash map: O(k).

Edge Cases

    k > len(arr):
        Return [].

    All elements are the same:
        Example: arr = [1, 1, 1], k = 2 → Output: [1, 1].

    All elements are distinct:
        Example: arr = [1, 2, 3, 4], k = 3 → Output: [3, 3].
'''