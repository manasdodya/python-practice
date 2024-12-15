'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-bonus-problems/problem/camelcase-pattern-matching2259

Given a dictionary of words arr[] where each word follows CamelCase notation, print all words in the dictionary that match with a given pattern pat consisting of uppercase characters only.

    CamelCase is the practice of writing compound words or phrases such that each word or abbreviation begins with a capital letter. Common examples include PowerPoint and Wikipedia, GeeksForGeeks, CodeBlocks, etc.

Example: "GeeksForGeeks" matches the pattern "GFG", because if we combine all the capital letters in "GeeksForGeeks" they become "GFG". Also note "GeeksForGeeks" matches with the pattern "GFG" and also "GF", but does not match with "FG".

Note: The driver code will sort your answer before checking and return the answer in any order.

Examples:

Input: arr[] = ["WelcomeGeek", "WelcomeToGeeksForGeeks", "GeeksForGeeks"], pat = "WTG"
Output: ["WelcomeToGeeksForGeeks"]
Explanation: Since only "WelcomeToGeeksForGeeks" matches the pattern, it is the only answer.

Input: arr[] = ["Hi", "Hello", "HelloWorld", "HiTech", "HiGeek", "HiTechWorld", "HiTechCity", "HiTechLab"], pat = "HA"
Output: []
Explanation: None of the words matches the given pattern.

Constraints:
1<= arr.size() <=1000
1<= pat.size() <=100
1<= arr[i].size() <=100
'''

def camel_case_match(arr, pat):
    result = []
    
    for word in arr:
        # Extract uppercase characters from the word
        uppercase_signature = ''.join([char for char in word if char.isupper()])
        
        # Check if the pattern matches the beginning of the uppercase signature
        if uppercase_signature.startswith(pat):
            result.append(word)
    
    return result

# Examples
arr1 = ["WelcomeGeek", "WelcomeToGeeksForGeeks", "GeeksForGeeks"]
pat1 = "WTG"
print(camel_case_match(arr1, pat1))  # Output: ["WelcomeToGeeksForGeeks"]

arr2 = ["Hi", "Hello", "HelloWorld", "HiTech", "HiGeek", "HiTechWorld", "HiTechCity", "HiTechLab"]
pat2 = "HA"
print(camel_case_match(arr2, pat2))  # Output: []

arr3 = ["GeeksForGeeks", "CodeBlocks", "PowerPoint", "Wikipedia"]
pat3 = "PP"
print(camel_case_match(arr3, pat3))  # Output: ["PowerPoint"]


'''
Approach:

    Extract the Uppercase Sequence:
        For each word, extract the sequence of uppercase letters.
        This sequence is the "CamelCase signature" of the word.

    Check for Pattern Match:
        Check if the pattern pat matches the start of the uppercase sequence extracted from each word.
        Use Python's string method .startswith() to verify the match.

    Collect Matches:
        Collect all words that match the pattern.

    Return Results:
        Return the collected words in any order (the driver code will sort them).

Explanation:

    Extracting Uppercase Letters:
        For a word like "GeeksForGeeks", the uppercase signature will be "GFG".
        This is done using a list comprehension:

        ''.join([char for char in word if char.isupper()])

    Pattern Matching:
        Using startswith, we ensure the pattern pat matches the beginning of the uppercase signature.

    Result Collection:
        If a word matches, it is added to the result list.

Complexity Analysis:

    Time Complexity:
        Extracting uppercase letters from each word: O(L), where L is the total length of all words combined.
        Checking the pattern match for each word: O(P), where P is the length of the pattern.
        Total complexity: O(L+N⋅P), where N is the number of words.

    Space Complexity:
        Result list stores up to N words: O(N⋅M), where M is the average word length.

'''