'''
URL :https://www.geeksforgeeks.org/batch/gfg-160-problems/track/two-pointer-technique-gfg-160/problem/longest-distinct-characters-in-string5848

Given a string s, find the length of the longest substring with all distinct characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.

Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.

Constraints:
1<= s.size()<=3*104
All the characters are in lowercase.

'''
def length_of_longest_substring(s):
    # Dictionary to store the last seen index of each character
    char_index = {}
    max_length = 0
    start = 0  # Start of the sliding window

    for end in range(len(s)):
        # If the character is in the map and its index is within the current window
        if s[end] in char_index and char_index[s[end]] >= start:
            # Move the start pointer to the right of the last occurrence of s[end]
            start = char_index[s[end]] + 1

        # Update the last seen index of the current character
        char_index[s[end]] = end

        # Calculate the length of the current window and update max_length
        max_length = max(max_length, end - start + 1)

    return max_length

# Example Usage
s1 = "geeksforgeeks"
s2 = "aaa"
s3 = "abcdefabcbb"

print("Output for s1:", length_of_longest_substring(s1))  # Output: 7
print("Output for s2:", length_of_longest_substring(s2))  # Output: 1
print("Output for s3:", length_of_longest_substring(s3))  # Output: 6


'''
Algorithm

    Initialize Variables:
        start: Marks the beginning of the current window.
        max_length: Stores the length of the longest substring found so far.
        char_index: A hash map (dictionary) to store the last occurrence of each character.

    Iterate Through the String:
        For each character s[end] at index end:
            If s[end] is already in char_index and its index is within the current window (start to end), 
            move start to char_index[s[end]] + 1 to ensure all characters in the window are distinct.
            Update char_index[s[end]] to the current index end.
            Calculate the length of the current window (end - start + 1) and update max_length if it's greater than the current max_length.

    Return the Result:
        After processing all characters, return max_length.

Example Walkthrough
Input: s = "geeksforgeeks"

    Initialize:
        start = 0, max_length = 0, char_index = {}.

    Process characters:
        end = 0, char = 'g': Add to char_index, max_length = 1.
        end = 1, char = 'e': Add to char_index, max_length = 2.
        end = 2, char = 'e': Found duplicate. Move start to 2, max_length = 2.
        Continue processing...

    Result:
        Longest substring: "eksforg", max_length = 7.

Complexity Analysis

    Time Complexity:
        Each character is processed at most twice (once when expanding end and possibly once when moving start).
        Total: O(n), where nn is the length of the string.

    Space Complexity:
        The char_index dictionary stores at most 26 entries (one for each lowercase letter).
        Total: O(1).

Edge Cases

    Empty string: s = "" → Output: 0.
    All unique characters: s = "abcdef" → Output: 6.
    All duplicates: s = "aaaaa" → Output: 1.
    Large input: Efficient for strings up to the constraint limit 
    .
'''