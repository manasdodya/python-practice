'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/check-if-strings-are-rotations-of-each-other-or-not-1587115620

You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.

Note: The characters in the strings are in lowercase.

Examples :

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.

Input: s1 = "aab", s2 = "aba"
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.

Input: s1 = "abcd", s2 = "acbd"
Output: false
Explanation: Strings are not rotations of each other.

Constraints:
1 <= s1.size(), s2.size() <= 105
'''

def is_rotation(s1, s2):
    # Step 1: Check if lengths are equal
    if len(s1) != len(s2):
        return False

    # Step 2: Concatenate s1 with itself
    doubled_s1 = s1 + s1

    # Step 3: Check if s2 is a substring of doubled_s1
    return s2 in doubled_s1

# Examples
print(is_rotation("abcd", "cdab"))  # Output: True
print(is_rotation("aab", "aba"))    # Output: True
print(is_rotation("abcd", "acbd"))  # Output: False

'''
Key Idea:

    If s2s2 is a rotated version of s1s1, then s2s2 will always be a substring of s1+s1s1+s1. This is because s1+s1s1+s1 contains all possible rotations of s1s1.

For example:

    s1="abcd"s1="abcd"
    s1+s1="abcdabcd"s1+s1="abcdabcd"
    All rotations of s1s1: "abcd", "bcda", "cdab", "dabc" are substrings of s1+s1s1+s1.

Algorithm:

    Check if s1s1 and s2s2 are of the same length. If not, return False.
    Concatenate s1s1 with itself to form s1+s1s1+s1.
    Check if s2s2 is a substring of s1+s1s1+s1.

Explanation of Examples:

    Input: s1 = "abcd", s2 = "cdab"
        s1+s1="abcdabcd"s1+s1="abcdabcd"
        s2="cdab"s2="cdab" is a substring of s1+s1s1+s1.
        Output: True.

    Input: s1 = "aab", s2 = "aba"
        s1+s1="aabaab"s1+s1="aabaab"
        s2="aba"s2="aba" is a substring of s1+s1s1+s1.
        Output: True.

    Input: s1 = "abcd", s2 = "acbd"
        s1+s1="abcdabcd"s1+s1="abcdabcd"
        s2="acbd"s2="acbd" is not a substring of s1+s1s1+s1.
        Output: False.

Complexity:

    Time Complexity:
        Checking substring: O(n), where n is the length of s1s1.
        Total: O(n).

    Space Complexity:
        O(n) for the concatenated string.

'''