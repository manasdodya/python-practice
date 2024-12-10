'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/implement-atoi

Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

    Skip any leading whitespaces.
    Check for a sign ('+' or '-'), default to positive if no sign is present.
    Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
    If the integer is greater than 231 - 1, then return 231 - 1 and if the integer is smaller than -231, then return -231.

Examples:

Input: s = "-123"
Output: -123
Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer

Input: s = "  -"
Output: 0
Explanation: No digits are present, therefore the returned answer is 0.

Input: s = " 1231231231311133"
Output: 2147483647
Explanation: The converted number will be greater than 231 - 1, therefore print 231 - 1 = 2147483647.

Input: s = "-999999999999"
Output: -2147483648
Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.

Input: s = "  -0012gfg4"
Output: -12
Explanation: Nothing is read after -12 as a non-digit character 'g' was encountered.

Constraints:
1 ≤ |s| ≤ 15

'''

def custom_atoi(s):
    # Constants for 32-bit signed integer range
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    # Step 1: Skip leading whitespaces
    i = 0
    n = len(s)
    while i < n and s[i] == ' ':
        i += 1

    # Step 2: Check for a sign
    sign = 1
    if i < n and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        i += 1

    # Step 3: Read digits and build the number
    result = 0
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')  # Convert character to digit
        # Check for overflow before multiplying
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + digit
        i += 1

    # Step 4: Apply the sign and return the result
    return sign * result

# Examples
print(custom_atoi("-123"))                # Output: -123
print(custom_atoi("  -"))                 # Output: 0
print(custom_atoi(" 1231231231311133"))   # Output: 2147483647
print(custom_atoi("-999999999999"))       # Output: -2147483648
print(custom_atoi("  -0012gfg4"))         # Output: -12


'''
Algorithm:

    Skip Leading Whitespaces:
        Traverse the string until you encounter a non-whitespace character.

    Check for a Sign:
        Determine if the number is positive or negative based on the presence of '+' or '-' after the whitespaces.

    Read Digits:
        Traverse the string, collecting numeric characters while ignoring leading zeros.
        Stop when a non-digit character is encountered.

    Handle No Digits:
        If no valid digits were read, return 0.

    Clamp the Result:
        Clamp the result to the range [-2^31,2^31 - 1][-2^31,2^31 - 1] to handle overflow.

Explanation of Examples:

    Input: "-123"
        After removing spaces: "-123".
        Sign: -1.
        Digits: 123.
        Result: -123.

    Input: " -"
        After removing spaces: "-".
        No digits found.
        Result: 0.

    Input: " 1231231231311133"
        After removing spaces: "1231231231311133".
        Sign: +1.
        Digits exceed INT_MAX.
        Result: 2147483647.

    Input: "-999999999999"
        After removing spaces: "-999999999999".
        Digits exceed INT_MIN.
        Result: -2147483648.

    Input: " -0012gfg4"
        After removing spaces: "-0012gfg4".
        Sign: -1.
        Digits: 12 (stops at g).
        Result: -12.

Complexity:

    Time Complexity: O(n), where nn is the length of the string. Each character is processed once.
    Space Complexity: O(1), as no extra space is used apart from a few variables.

'''