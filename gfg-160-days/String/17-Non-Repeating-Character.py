'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/non-repeating-character-1587115620

Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.

Examples:

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.

Input: s = "racecar"
Output: 'e'
Explanation: In the given string, 'e' is the only character in the string which does not repeat.

Input: s = "aabbccc"
Output: -1
Explanation: All the characters in the given string are repeating.

Constraints:
1 <= s.size() <= 105

'''

def first_non_repeating(s):
    # Step 1: Count frequencies of characters
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Step 2: Find the first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char

    # Step 3: Return '$' if no non-repeating character exists
    return '$'

# Examples
print(first_non_repeating("geeksforgeeks"))  # Output: 'f'
print(first_non_repeating("racecar"))        # Output: 'e'
print(first_non_repeating("aabbccc"))        # Output: '$'

'''
Algorithm:

    Count Frequencies:
        Use a dictionary to store the frequency of each character in the string.

    Find the First Non-Repeating Character:
        Traverse the string again, and for each character, check its frequency in the dictionary.
        Return the first character with a frequency of 1.

    Handle No Non-Repeating Characters:
        If no such character is found, return '$'.

Explanation of Examples:

    Input: s = "geeksforgeeks"
        Frequencies:

    freq = {'g': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}

    The first character with frequency 1 is 'f'.

Input: s = "racecar"

    Frequencies:

    freq = {'r': 2, 'a': 2, 'c': 2, 'e': 1}

    The first character with frequency 1 is 'e'.

Input: s = "aabbccc"

    Frequencies:

        freq = {'a': 2, 'b': 2, 'c': 3}

        No character with frequency 1, so return '$'.

Complexity:

    Time Complexity:
        O(n) for counting frequencies (single pass over the string).
        O(n) for finding the first non-repeating character (another pass over the string).
        Total: O(n).

    Space Complexity:
        O(k), where kk is the number of distinct characters in the string (up to 26 for lowercase Latin letters).

'''