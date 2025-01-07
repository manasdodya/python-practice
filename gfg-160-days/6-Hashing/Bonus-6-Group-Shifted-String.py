'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-bonus-problem/problem/group-shifted-string

Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group are shifted versions of each other.

Two strings s1 and s2 are called shifted if the following conditions are satisfied:

    s1.length = s2.length
    s1[i] = s2[i] + m for 1 <= i <= s1.length  for a constant integer m

Examples :

Input: arr = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
Output: [["acd", "dfg", "wyz", "yab", "mop"], ["bdfh", "moqs"], ["a", "x"]] 
Explanation: All shifted strings are grouped together.

Input: arr = ["geek", "for", "geeks"]
Output: [["for"], ["geek"], ["geeks"]]

Input: arr = ["aaa", "adb", "bbd", "dbc", "bca"]
Output: [["aaa"], ["adb"], ["bbd"], ["bca"], ["dbc"]]

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i].size() ≤ 5
'''

def groupShiftedStrings(arr):
    from collections import defaultdict

    # Dictionary to group strings by their "shift key"
    groups = defaultdict(list)

    for s in arr:
        if len(s) == 1:
            # Single character strings all belong to unique groups
            key = (0,)
        else:
            # Calculate the key as differences between adjacent characters
            key = tuple((ord(s[i+1]) - ord(s[i])) % 26 for i in range(len(s) - 1))
        
        # Add the string to the group corresponding to its key
        groups[key].append(s)

    # Return the grouped strings as a list of lists
    return list(groups.values())

# Examples
print(groupShiftedStrings(["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]))
# Output: [["acd", "dfg", "wyz", "yab", "mop"], ["bdfh", "moqs"], ["a", "x"]]

print(groupShiftedStrings(["geek", "for", "geeks"]))
# Output: [["for"], ["geek"], ["geeks"]]

print(groupShiftedStrings(["aaa", "adb", "bbd", "dbc", "bca"]))
# Output: [["aaa"], ["adb"], ["bbd"], ["bca"], ["dbc"]]


'''
Key Idea

Strings are shifted versions of each other if the relative difference between adjacent characters remains the same for all characters in the string. For example:

    "acd" and "dfg" are shifted versions because the differences are [2, 3] in both strings.

Steps

    Generate a Key:
        For each string, compute the relative differences between adjacent characters as a key. For example:
            For "acd", the differences are [2, 3].
            These differences uniquely identify the group to which the string belongs.
        Handle cyclic shifts using modulo 26 for alphabet wrapping.

    Group by Key:
        Use a dictionary to store groups of strings, where the key is the computed difference and the value is a list of strings belonging to that group.

    Output Groups:
        Collect all the values (groups of strings) from the dictionary.

Algorithm

    Initialization:
        Create an empty dictionary to store the groups.
    Compute Key for Each String:
        If a string has length 1, its key is constant (e.g., "a" or "x").
        Otherwise, calculate the relative differences between adjacent characters, considering modulo 26.
    Store in Dictionary:
        Append each string to the list corresponding to its key.
    Return Groups:
        Convert the dictionary values to a list of lists.

Explanation of Examples
Example 1:

Input: ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]

    Keys:
        "acd" → (2, 3)
        "dfg" → (2, 3)
        "wyz" → (2, 3)
        "yab" → (2, 3)
        "mop" → (2, 3)
        "bdfh" → (2, 2, 2)
        "a" → (0,)
        "x" → (0,)
        "moqs" → (2, 2, 2)
    Groups:
        Group 1: ["acd", "dfg", "wyz", "yab", "mop"]
        Group 2: ["bdfh", "moqs"]
        Group 3: ["a", "x"]
    Output: [['acd', 'dfg', 'wyz', 'yab', 'mop'], ['bdfh', 'moqs'], ['a', 'x']].

Complexity Analysis

    Time Complexity:
        Key Calculation: For a string of length L, computing the key takes O(L).
        Total Key Calculation: O(sum of lengths of all strings)=O(n⋅avg_len)
        Insertion into the dictionary is O(1) per string.
        Total: O(n⋅avg_len), where nn is the number of strings.

    Space Complexity:
        Dictionary storage: O(n) for nn strings.



'''