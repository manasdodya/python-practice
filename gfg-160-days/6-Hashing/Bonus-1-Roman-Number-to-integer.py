'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-bonus-problem/problem/roman-number-to-integer3201

Given a string in Roman number format (s), your task is to convert it to an integer. Various symbols and their values are given below.
Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

Examples:

Input: s = "IX"
Output: 9
Explanation: IX is a Roman symbol which represents 10 – 1 = 9.

Input: s = "XL" 
Output: 40
Explanation: XL is a Roman symbol which represents 50 – 10 = 40.

Input: s = "MCMIV" 
Output: 1904
Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904.

Constraints:
1<= roman number <=3999
s[i] belongs to [I, V, X, L, C, D, M]
'''
def romanToInteger(s):
    # Roman numeral mapping
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    n = len(s)
    total = 0
    
    for i in range(n):
        # If this numeral is smaller than the next, subtract it
        if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            # Otherwise, add it
            total += roman_map[s[i]]
    
    return total

# Examples
print(romanToInteger("IX"))    # Output: 9
print(romanToInteger("XL"))    # Output: 40
print(romanToInteger("MCMIV")) # Output: 1904

'''
Algorithm

    Create a mapping of Roman numerals to their integer values.
    Traverse the string from left to right:
        If the current numeral's value is less than the next numeral's value, subtract the current numeral's value from the total.
        Otherwise, add the current numeral's value to the total.
    Add the value of the last numeral (since there is no next numeral to compare for subtraction).

Explanation with Example

For s = "MCMIV":

    M = 1000, so add 1000. Total = 1000.
    C = 100, M = 1000. Since 100 < 1000, subtract 100. Total = 900.
    M = 1000, so add 1000. Total = 1900.
    I = 1, V = 5. Since 1 < 5, subtract 1. Total = 1904.
    V = 5, so add 5. Total = 1904.

Time and Space Complexity

    Time Complexity: O(n), where nn is the length of the Roman numeral string.
    Space Complexity: O(1), since the mapping table is of constant size.
'''