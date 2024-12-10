'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-bonus-problems/problem/number-to-words0335

Write a function to convert a given number n into words.

    The idea is to break down the number into International Number System, i.e., smaller groups of three digits (hundreds, tens, and ones), and convert each group into words.

Examples :

Input: n = 0
Output: "Zero"

Input: n = 123
Output: "One Hundred Twenty Three"

Input: n = 10245
Output: "Ten Thousand Two Hundred Forty Five"

Input: n = 2147483647
Output: "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"

Constraints:
0 <= n <= 231-1

'''

def numberToWords(n):
    # Mapping for numbers from 0 to 19 and multiples of 10
    less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
                     "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                     "Seventeen", "Eighteen", "Nineteen"]
    
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    thousands = ["", "Thousand", "Million", "Billion"]

    # Helper function to convert a number less than 1000 to words
    def helper(n):
        if n == 0:
            return ""
        elif n < 20:
            return less_than_20[n]
        elif n < 100:
            return tens[n // 10] + " " + less_than_20[n % 10] if n % 10 != 0 else tens[n // 10]
        else:
            return less_than_20[n // 100] + " Hundred " + helper(n % 100) if n % 100 != 0 else less_than_20[n // 100] + " Hundred"

    # Edge case for 0
    if n == 0:
        return "Zero"

    result = []
    i = 0  # To handle the powers of 1000 (Thousand, Million, Billion)
    
    # Process the number in chunks of 1000
    while n > 0:
        if n % 1000 != 0:
            result.insert(0, helper(n % 1000) + " " + thousands[i] if thousands[i] != "" else helper(n % 1000))
        n //= 1000
        i += 1

    # Strip trailing spaces and return the result
    return ' '.join(result).strip()

# Test cases
print(numberToWords(0))  # "Zero"
print(numberToWords(123))  # "One Hundred Twenty Three"
print(numberToWords(10245))  # "Ten Thousand Two Hundred Forty Five"
print(numberToWords(2147483647))  # "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"


