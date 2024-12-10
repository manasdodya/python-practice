'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/minimum-characters-to-be-added-at-front-to-make-string-palindrome

Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

Note: A palindrome string is a sequence of characters that reads the same forward and backward.

Examples:

Input: s = "abc"
Output: 2
Explanation: Add 'b' and 'c' at front of above string to make it palindrome : "cbabc"

Input: s = "aacecaaaa"
Output: 2
Explanation: Add 2 a's at front of above string to make it palindrome : "aaaacecaaaa"

Constraints:
1 <= s.size() <= 106

'''
def min_chars_to_make_palindrome(s):
    # Create a concatenated string with a separator
    concatenated = s + '#' + s[::-1]

    # Compute the LPS array
    lps = [0] * len(concatenated)
    for i in range(1, len(concatenated)):
        length = lps[i - 1]
        while length > 0 and concatenated[i] != concatenated[length]:
            length = lps[length - 1]
        if concatenated[i] == concatenated[length]:
            length += 1
        lps[i] = length

    # Calculate the minimum characters to add
    return len(s) - lps[-1]

# Examples
print(min_chars_to_make_palindrome("abc"))        # Output: 2
print(min_chars_to_make_palindrome("aacecaaaa"))  # Output: 2


'''
Key Idea:

    Palindrome Property:
        To make a string palindrome by adding characters at the front, we need to identify the longest prefix of the string that is also a suffix of its reverse. The remaining portion must be added at the front.

    Efficient Calculation with LPS:
        Concatenate the original string s with its reverse using a separator (e.g., s + '#' + reverse(s)).
        Compute the LPS array for the concatenated string to find the longest prefix that is also a suffix.

    Result:
        The number of characters to add is equal to the length of the original string minus the LPS value of the last character in the concatenated string.

Explanation of Examples:

    Input: s = "abc"
        Concatenated string: "abc#cba"
        LPS array: [0, 0, 0, 0, 1, 2, 3]
        LPS value at last character=3LPS value at last character=3
        Minimum characters to add: 3-3=23-3=2.

    Input: s = "aacecaaaa"
        Concatenated string: "aacecaaaa#aaacecaa"
        LPS array: [0, 1, 0, 0, 1, 2, 2, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        LPS value at last character=8LPS value at last character=8
        Minimum characters to add: 9-8=29-8=2.

Complexity:

    Time Complexity:O(n) for computing the LPS array, where n=2*len(s)+1n=2*len(s)+1.
    Space Complexity:O(n) for the concatenated string and the LPS array.

'''