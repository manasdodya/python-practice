'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/search-pattern0205

Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
Note: Return an empty list in case of no occurrences of pattern.

Examples :

Input: txt = "abcab", pat = "ab"
Output: [0, 3]
Explanation: The string "ab" occurs twice in txt, one starts at index 0 and the other at index 3. 

Input: txt = "abesdu", pat = "edu"
Output: []
Explanation: There's no substring "edu" present in txt.

Input: txt = "aabaacaadaabaaba", pat = "aaba"
Output: [0, 9, 12]
Explanation:

Constraints:
1 ≤ txt.size() ≤ 106
1 ≤ pat.size() < txt.size()
Both the strings consist of lowercase English alphabets.

'''
def find_pattern_occurrences(txt, pat):
    # Step 1: Compute the LPS array
    def compute_lps(pat):
        lps = [0] * len(pat)
        length = 0  # Length of the previous longest prefix suffix
        i = 1  # Start from the second character in the pattern
        
        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Fallback in the prefix
                    length = lps[length - 1]
                else:
                    # No prefix match
                    lps[i] = 0
                    i += 1
        return lps
    
    # Step 2: KMP Search
    lps = compute_lps(pat)
    i = 0  # Index for txt
    j = 0  # Index for pat
    indices = []

    while i < len(txt):
        if txt[i] == pat[j]:
            i += 1
            j += 1
        if j == len(pat):
            # Pattern found
            indices.append(i - j)
            j = lps[j - 1]
        elif i < len(txt) and txt[i] != pat[j]:
            # Mismatch after j matches
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

# Examples
print(find_pattern_occurrences("abcab", "ab"))         # Output: [0, 3]
print(find_pattern_occurrences("abesdu", "edu"))       # Output: []
print(find_pattern_occurrences("aabaacaadaabaaba", "aaba"))  # Output: [0, 9, 12]


'''
Algorithm:

    Precompute the LPS Array:
        The LPS (Longest Prefix Suffix) array is computed for the pattern string. This array tells us the length of the longest prefix which is also a suffix for each position in the pattern.
        The LPS array helps us avoid rechecking characters that have already been matched.

    Search the Pattern in the Text:
        Traverse the text while comparing it to the pattern. Use the LPS array to shift the pattern efficiently when a mismatch occurs.
        Record the starting index of every match.

    Handle No Matches:
        If no matches are found, return an empty list.

Explanation of Examples:

    Input: txt = "abcab", pat = "ab"
        Matches at indices 0 and 3.

    Input: txt = "abesdu", pat = "edu"
        No match, return [].

    Input: txt = "aabaacaadaabaaba", pat = "aaba"
        Matches at indices 0, 9, and 12.

Complexity:

    Precomputing LPS Array: O(m), where m is the length of the pattern.
    Pattern Search: O(n), where n is the length of the text.
    Overall Time Complexity: O(n+m).
    Space Complexity: O(m)O for the LPS array.
'''