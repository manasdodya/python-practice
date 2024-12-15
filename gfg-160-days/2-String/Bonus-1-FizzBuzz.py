'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-bonus-problems/problem/fizz-buzz

Fizz Buzz Problem involves that given an integer n, for every integer 0 < i <= n, the task is to output,

    "FizzBuzz" if i is divisible by 3 and 5,
    "Fizz" if i is divisible by 3,
    "Buzz" if i is divisible by 5
    "i" as a string, if none of the conditions are true.

Return an array of strings.

Examples :

Input: n = 3
Output: ["1", "2", "Fizz"]
Explanation: 1 and 2 are neither divisible by 3 nor 5, so we just output 1 and 2, and 3 is divisible by 3 so we output "Fizz".

Input: n = 10
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]

Input: n = 20
Output: [“1”, “2”, “Fizz”, “4”, “Buzz”, “Fizz”, “7”, “8”, “Fizz”, “Buzz”, “11”, “Fizz”, “13”, “14”, “FizzBuzz”, “16”, “17”, “Fizz”, “19”, “Buzz”]

Constraints:
1 ≤ n ≤ 106
'''

def fizz_buzz_with_dict(n):
    result = []
    fizz_buzz_map = {3: "Fizz", 5: "Buzz"}  # Define the mapping

    for i in range(1, n + 1):
        output = ""
        for divisor, word in fizz_buzz_map.items():
            if i % divisor == 0:
                output += word
        
        # If no match, use the number itself
        result.append(output if output else str(i))
    
    return result

# Examples
print(fizz_buzz_with_dict(3))   # Output: ["1", "2", "Fizz"]
print(fizz_buzz_with_dict(10))  # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
print(fizz_buzz_with_dict(20))  # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"]

'''
Approach Using Dictionary:

    Define a dictionary with divisors as keys and corresponding outputs as values.
        Example: {3: "Fizz", 5: "Buzz"}.
    Iterate through numbers from 1 to nn:
        For each number, check all keys in the dictionary.
        Concatenate the corresponding outputs for each divisor that the number is divisible by.
        If no divisors match, append the number itself as a string.
    Return the result list.

Explanation of Code:

    Dictionary Usage:
        The dictionary fizz_buzz_map contains:
            3→"Fizz"3→"Fizz"
            5→"Buzz"5→"Buzz"
        This allows for easy extension. For example, adding a rule for 7→"Boom"7→"Boom" would only require updating the dictionary.

    Concatenation Logic:
        For each number, iterate through the dictionary to check divisibility.
        Concatenate outputs for matching divisors. For instance:
            i=15: Divisible by both 3 and 5, so "Fizz" + "Buzz" → "FizzBuzz".
            i=3: Divisible by 3, so "Fizz".

    Fallback to String Representation:
        If no divisors match, use the string representation of the number.

        omplexity Analysis:

    Time Complexity:
        Outer loop: O(n) for nn iterations.
        Inner loop: O(k), where k is the number of divisors in the dictionary (constant for typical use cases).
        Total: O(n).

    Space Complexity:
        Result list: O(n).
        Dictionary size: O(k), where k is typically small.
'''
