'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/array-bonus-problems/problem/repetitive-addition-of-digits2221

You are given a positive integer n, you need to add all the digits of n and create a new number. Perform this operation until the resultant number has only one digit in it. Return the final number obtained after performing the given operation.

Examples:

Input: n = 1234
Output: 1
Explanation: Step 1: 1 + 2 + 3 + 4 = 10. Step 2: 1 + 0 = 1

Input: n = 5674
Output: 4
Explanation: Step 1: 5 + 6 + 7 + 4 = 22. Step 2: 2 + 2 = 4

Input: n = 9
Output: 9
Explanation: Since 9 is a single-digit number hence we return 9.

Constraints:
1 <= n <= 109

'''

def addDigits(n):
    # If n is 0, return 0
    if n == 0:
        return 0
    # Return n % 9, but if it's 0, return 9
    return 9 if n % 9 == 0 else n % 9

# Test examples
print(addDigits(1234))  # Output: 1
print(addDigits(5674))  # Output: 4
print(addDigits(9))     # Output: 9

'''
Key Insights:

The digital root can be computed using the following formula:

    If n=0n=0, the result is 0.
    Otherwise, the result is n mod 9.
        If the result is 0 and n>0n>0, then the digital root is 9 (since numbers like 9, 18, 27, etc., yield 0 modulo 9 but should return 9).
        Otherwise, the result is simply n mod 9.

Why does this work?

This method relies on a property of numbers in number theory known as casting out nines. The digital root is essentially the remainder when the number is divided by 9, with a slight adjustment when the remainder is 0.
Approach:

    If n=0n=0, return 0.
    Otherwise, return n mod 9, and if that is 0, return 9.

Explanation:

    For n = 1234:
        The sum of the digits is 10, and the sum of the digits of 10 is 1. So, the result is 1.
    For n = 5674:
        The sum of the digits is 22, and the sum of the digits of 22 is 4. So, the result is 4.
    For n = 9:
        Since it's a single digit, we directly return 9.

Time Complexity: O(1): The solution runs in constant time as it only involves simple mathematical operations (modulus and conditional checks).

Space Complexity: O(1): The solution uses only a few variables to store intermediate results, and no extra space is used.

'''


'''
Alternate code
def singleDigit(n):
    sum = 0

    # Repetitively calculate sum until
    # it becomes single digit
    while n > 0 or sum > 9:

        # If n becomes 0, reset it to sum 
        # and start a new iteration
        if n == 0:
            n = sum
            sum = 0

        sum += n % 10
        n //= 10
    return sum

if __name__ == "__main__":
    n = 1234
    print(singleDigit(n))
'''