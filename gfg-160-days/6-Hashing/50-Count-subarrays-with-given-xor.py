'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/count-subarray-with-given-xor

Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

Examples: 

Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.

Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.

Input: arr[] = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].

Constraints:

    1 ≤ arr.size() ≤ 105
    0 ≤ arr[i] ≤105
    0 ≤ k ≤ 105
'''

def subarrayXOR(arr, k):
    # Initialize a hashmap to store the frequency of prefix XORs
    prefix_XOR_count = {0: 1}  # To account for the case where the XOR equals k starting from the beginning
    current_prefix_XOR = 0
    count = 0
    
    # Traverse the array
    for num in arr:
        current_prefix_XOR ^= num  # Update the current prefix XOR
        
        # Check if current_prefix_XOR ^ k exists in the hashmap
        if current_prefix_XOR ^ k in prefix_XOR_count:
            count += prefix_XOR_count[current_prefix_XOR ^ k]  # Increment count by the frequency of the XOR
        
        # Update the frequency of the current prefix XOR in the hashmap
        if current_prefix_XOR in prefix_XOR_count:
            prefix_XOR_count[current_prefix_XOR] += 1
        else:
            prefix_XOR_count[current_prefix_XOR] = 1
    
    return count

# Test cases
print(subarrayXOR([4, 2, 2, 6, 4], 6))  # Output: 4
print(subarrayXOR([5, 6, 7, 8, 9], 5))  # Output: 2
print(subarrayXOR([1, 1, 1, 1], 0))     # Output: 4


'''
Explanation of the Approach:

    Prefix XOR:
        The prefix XOR up to index i is the XOR of all elements from the beginning of the array to index i.
        For any subarray arr[l...r], the XOR of that subarray is:
        XOR(arr[l...r])=prefix_XOR[r]⊕prefix_XOR[l−1]
        XOR(arr[l...r])=prefix_XOR[r]⊕prefix_XOR[l−1]
        If this XOR is equal to k, we have found a subarray that has an XOR equal to k.

    Hashmap (or Dictionary):
        We use a hashmap to store how many times each prefix XOR has occurred as we iterate through the array.
        At each index i, we compute the current prefix XOR. If current_prefix_XOR ^ k has been encountered before, it means there exists a subarray ending at index i that has an XOR equal to k.
        The frequency of current_prefix_XOR ^ k in the hashmap tells us how many such subarrays end at the current index.

    Steps:
        Initialize current_prefix_XOR = 0 and a hashmap to store the frequency of prefix XORs. Initially, store {0: 1} to account for the case where a subarray starting from the beginning of the array has XOR equal to k.
        Traverse the array, updating the prefix XOR at each step.
        If current_prefix_XOR ^ k is present in the hashmap, it means there are one or more subarrays ending at the current index that have XOR equal to k. We increment the count by the frequency of current_prefix_XOR ^ k.
        Update the hashmap with the current prefix XOR.

Time Complexity:

    The time complexity is O(n) because we are iterating over the array once, and each operation (hashmap lookup and insertion) takes O(1) time on average.

Space Complexity:

    The space complexity is O(n) because we are storing the frequency of prefix XORs in the hashmap.

Explanation of Code:

    prefix_XOR_count = {0: 1}:
        This is initialized to store the frequency of prefix XORs, with {0: 1} to account for the edge case where the XOR of a subarray starting from the beginning is equal to k.

    current_prefix_XOR ^= num:
        This updates the current prefix XOR as we traverse the array. The XOR operation is performed between the previous current_prefix_XOR and the current element num.

    if current_prefix_XOR ^ k in prefix_XOR_count:
        This checks if there exists a previous prefix XOR such that the XOR between current_prefix_XOR and k is in the hashmap. If it exists, it means there are one or more subarrays ending at the current index that have XOR equal to k, and we increment the count by the frequency of current_prefix_XOR ^ k.

    prefix_XOR_count[current_prefix_XOR] += 1:
        After processing the current element, we update the frequency of the current prefix XOR in the hashmap.

Example Walkthrough:

For the input array arr = [4, 2, 2, 6, 4] and k = 6:

    Initially, prefix_XOR_count = {0: 1}, current_prefix_XOR = 0, count = 0.

    First element (4):
        current_prefix_XOR = 4
        No match (4 ^ 6 = 2 not in hashmap).
        Update hashmap: prefix_XOR_count = {0: 1, 4: 1}.

    Second element (2):
        current_prefix_XOR = 6
        Match (6 ^ 6 = 0 is in hashmap, 1 occurrence).
        Increment count: count = 1.
        Update hashmap: prefix_XOR_count = {0: 1, 4: 1, 6: 1}.

    Third element (2):
        current_prefix_XOR = 4
        Match (4 ^ 6 = 2 is in hashmap, 1 occurrence).
        Increment count: count = 2.
        Update hashmap: prefix_XOR_count = {0: 1, 4: 2, 6: 1}.

    Fourth element (6):
        current_prefix_XOR = 2
        No match (2 ^ 6 = 4 is in hashmap, 2 occurrences).
        Increment count: count = 4.
        Update hashmap: prefix_XOR_count = {0: 1, 4: 2, 6: 1, 2: 1}.

    Fifth element (4):
        current_prefix_XOR = 6
        Match (6 ^ 6 = 0 is in hashmap, 1 occurrence).
        Increment count: count = 5.
        Update hashmap: prefix_XOR_count = {0: 1, 4: 2, 6: 2, 2: 1}.

Final count is 5, which is the correct answer.

'''