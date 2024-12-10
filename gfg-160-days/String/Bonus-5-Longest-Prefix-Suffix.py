'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-bonus-problems/problem/longest-prefix-suffix2527

Given a string of characters s, find the length of the longest prefix which is also a suffix.
Note: Prefix and suffix can be overlapping but they should not be equal to the entire string.

Examples :

Input: s = "abab"
Output: 2
Explanation: "ab" is the longest prefix and suffix. 

Input: s = "aabcdaabc"
Output: 4
Explanation: The string "aabc" is the longest prefix and suffix.

Input: s = "aaaa"
Output: 3
Explanation: "aaa" is the longest prefix and suffix. 

Constraints:
1 ≤ s.size() ≤ 106
s contains only lowercase English alphabets.

'''
def longestPrefixSuffix(s):
    n = len(s)
    lps = [0] * n
    
    # len stores the length of longest prefix which
    # is also a suffix for the previous index
    length = 0

    # lps[0] is always 0
    lps[0] = 0

    i = 1
    while i < n:

        # If characters match, increment the size of lps
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        # If there is a mismatch
        else:
            if length != 0:

                # Update length to the previous lps value
                # to avoid redundant comparisons
                length = lps[length - 1]
            else:
              
                # If no matching prefix found, set lps[i] to 0
                lps[i] = 0
                i += 1
    
    # Last element of lps array will store the length of
    # longest prefix that is also suffix of entire string
    return lps[n - 1]
 
print(longestPrefixSuffix("ababab"))  # Output: 4
print(longestPrefixSuffix("aabcdaabc"))  # Output: 4
print(longestPrefixSuffix("aaaa"))  # Output: 3

'''
Approach:

    Prefix Function (LPS Array): The prefix function is an array lps[] where each element lps[i] represents the length of the longest proper prefix (prefix which is not equal to the entire string) which is also a suffix for the substring s[0...i].

    Key Observations:
        The last value in the lps array (lps[len(s) - 1]) gives us the length of the longest prefix that matches a suffix for the entire string.
        However, we need to ensure that this prefix is not equal to the entire string. So, if lps[len(s) - 1] == len(s), we should ignore this value because it means the entire string is both a prefix and a suffix.

    Steps:
        We can compute the lps array for the given string s.
        The value of lps[len(s) - 1] will give us the longest prefix-suffix. If it is equal to the length of the string, we take the next largest value from the lps array to ensure that the prefix is proper (i.e., the entire string is not considered as a prefix and suffix).

Algorithm:

    Initialize an array lps[] of the same size as the string.
    Use a two-pointer technique to build the lps array.
    Once the lps array is built, the value at the last index gives us the answer.

Explanation:

    LPS Array Calculation:
        We initialize the lps array to store the length of the longest proper prefix which is also a suffix.
        The loop iterates over the string starting from the second character, checking for matches with previous characters in the prefix and suffix.
        If a match is found, the length of the matching prefix-suffix is updated. If no match is found, we fall back to a shorter prefix using the previously computed values in the lps array.

    Final Check:
        Once the lps array is populated, the last element (lps[n - 1]) gives the length of the longest prefix which is also a suffix.
        If this value is equal to the length of the string (n), we know that the entire string is a prefix and suffix, which we want to avoid, so we return the value from the previous position in the lps array (lps[lps[n - 1] - 1]).

Time Complexity: O(n) where n is the length of the string s. The time complexity is linear because we are only iterating over the string once and processing each character in constant time using the lps array.

Space Complexity: O(n) for storing the lps array.

Example Walkthrough:

    Input: "abab"
        The LPS array will be computed as [0, 0, 1, 2].
        The longest prefix which is also a suffix is of length 2 ("ab").
        Output: 2.

    Input: "aabcdaabc"
        The LPS array will be computed as [0, 1, 0, 1, 2, 3, 4, 0, 1].
        The longest prefix which is also a suffix is of length 4 ("aabc").
        Output: 4.

    Input: "aaaa"
        The LPS array will be computed as [0, 1, 2, 3].
        The longest prefix which is also a suffix is of length 3 ("aaa").
        Output: 3.
'''