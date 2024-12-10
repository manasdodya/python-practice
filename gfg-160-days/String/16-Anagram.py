'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/anagram-1587115620

Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

Note: You can assume both the strings s1 & s2 are non-empty.

Examples :

Input: s1 = "geeks", s2 = "kseeg"
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = "allergy", s2 = "allergic"
Output: false
Explanation: Characters in both the strings are not same, so they are not anagrams.

Input: s1 = "g", s2 = "g"
Output: true
Explanation: Character in both the strings are same, so they are anagrams.

Constraints:
1 ≤ s1.size(), s2.size() ≤ 105
'''

def are_anagrams(s1, s2):
    # Step 1: Check if lengths are equal
    if len(s1) != len(s2):
        return False

    # Step 2: Initialize dictionaries for character counts
    freq1 = {}
    freq2 = {}

    # Step 3: Count frequencies for both strings
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1

    # Step 4: Compare the two frequency dictionaries
    return freq1 == freq2

# Examples
print(are_anagrams("geeks", "kseeg"))      # Output: True
print(are_anagrams("allergy", "allergic")) # Output: False
print(are_anagrams("g", "g"))              # Output: True


'''
Algorithm:

    Check Lengths:
        If the lengths of the two strings are different, they cannot be anagrams.

    Count Frequencies:
        Use a dictionary to count the frequency of each character in both strings.

    Compare Dictionaries:
        If the two dictionaries are identical, the strings are anagrams. Otherwise, they are not.

Explanation of Examples:

    Input: s1 = "geeks", s2 = "kseeg"
        Frequencies:

    freq1 = {'g': 1, 'e': 2, 'k': 1, 's': 1}
    freq2 = {'k': 1, 's': 1, 'e': 2, 'g': 1}

    freq1 == freq2, so the strings are anagrams.

Input: s1 = "allergy", s2 = "allergic"

    Lengths differ, so the strings cannot be anagrams.

Input: s1 = "g", s2 = "g"

    Frequencies:

        freq1 = {'g': 1}
        freq2 = {'g': 1}

        freq1 == freq2, so the strings are anagrams.

Complexity:

    Time Complexity:
        O(n), where n=max(len(s1),len(s2)). Each character is processed once.

    Space Complexity:
        O(k), where k is the number of distinct characters in the string (up to 26 for lowercase alphabets).

'''