'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/add-binary-strings3805

Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100

Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110

Constraints:
1 ≤s1.size(), s2.size()≤ 106
'''

def add_binary_strings(s1, s2):
    # Make the strings the same length by padding with leading zeros
    max_len = max(len(s1), len(s2))
    s1 = s1.zfill(max_len)
    s2 = s2.zfill(max_len)

    carry = 0
    result = []

    # Traverse both strings from right to left
    for i in range(max_len - 1, -1, -1):
        bit1 = int(s1[i])  # Convert character to integer
        bit2 = int(s2[i])
        total = bit1 + bit2 + carry
        result.append(total % 2)  # Result bit
        carry = total // 2        # Carry bit

    # If there's a carry left, add it to the result
    if carry:
        result.append(carry)

    # Reverse the result and convert to a string
    result.reverse()
    return ''.join(map(str, result)).lstrip('0') or '0'  # Remove leading zeros

# Examples
print(add_binary_strings("1101", "111"))     # Output: "10100"
print(add_binary_strings("00100", "010"))    # Output: "110"
print(add_binary_strings("0", "0"))          # Output: "0"

'''
Algorithm:

    Normalize Lengths:
        Pad the shorter string with leading zeros to make both strings the same length.

    Perform Binary Addition:
        Start from the least significant bit (rightmost bit) and move to the most significant bit.
        For each pair of bits:
            Compute the sum of the two bits and the carry.
            Determine the resulting bit (sum % 2).
            Update the carry (sum // 2).

    Handle Remaining Carry:
        If there's a carry left after processing all bits, prepend it to the result.

    Remove Leading Zeros:
        Strip leading zeros from the result to ensure no unnecessary zeros remain.

Explanation of Examples:

    Input: s1 = "1101", s2 = "111"
        After padding: s1 = "1101", s2 = "0111".
        Binary addition:

      1101
    + 0111
    ------
     10100

    Result: "10100".

Input: s1 = "00100", s2 = "010"

    After padding: s1 = "00100", s2 = "00010".
    Binary addition:

      00100
    + 00010
    ------
       110

    Result: "110".

Input: s1 = "0", s2 = "0"

    No padding needed.
    Binary addition:

          0
        + 0
        ---
          0

        Result: "0".

Complexity:

    Time Complexity: O(n), where nn is the maximum length of the two strings.
    Space Complexity: O(n), for storing the result.
'''