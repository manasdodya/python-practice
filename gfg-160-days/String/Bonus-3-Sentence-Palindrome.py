'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-bonus-problems/problem/string-palindromic-ignoring-spaces4723

Given a single string s, the task is to check if it is a palindrome sentence or not. A palindrome sentence is a sequence of characters, such as word, phrase, or series of symbols that reads the same backward as forward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

Examples:

Input: s = "Too hot to hoot"
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become “toohottohoot” which is a palindrome.

Input: s = "Abc 012..## 10cbA"
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become “abc01210cba” which is a palindrome.

Input: s = "ABC $. def01ASDF"
Output: false
Explanation: The processed string becomes "abcdef01asdf", which is not a palindrome.

Constraints:
1<= s.size() <= 106
'''
def is_palindrome_sentence(s):
    # Step 1: Filter non-alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Check for palindrome using two-pointer technique
    left, right = 0, len(filtered) - 1
    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Examples
print(is_palindrome_sentence("Too hot to hoot"))        # Output: True
print(is_palindrome_sentence("Abc 012..## 10cbA"))      # Output: True
print(is_palindrome_sentence("ABC $. def01ASDF"))       # Output: False

'''
Steps to Solve:

    Filter the Input:
        Remove all non-alphanumeric characters using Python's string methods or regular expressions.
        Convert all characters to lowercase.

    Check for Palindrome:
        Use two pointers (left and right) to traverse the string from both ends.
        Compare characters at the left and right pointers.
        If all characters match, it's a palindrome.

Explanation of Code:

    Filtering Characters:
        char.isalnum() checks if a character is alphanumeric (letters or digits).
        char.lower() converts uppercase letters to lowercase.
        ''.join(...) rebuilds the string after filtering.

    Two-Pointer Technique:
        Compare the first (left) and last (right) characters.
        Move left forward and right backward until they meet.
        If all characters match, the string is a palindrome.

Complexity Analysis:

    Time Complexity:
        Filtering: O(n), where n is the length of the input string.
        Palindrome check: O(m), where m is the length of the filtered string (m≤n).
        Total: O(n).

    Space Complexity:
        The filtered string requires O(m) space.
'''