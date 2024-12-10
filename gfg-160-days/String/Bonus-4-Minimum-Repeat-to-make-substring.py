'''
URL - https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-bonus-problems/problem/minimum-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it--170645

Given two strings s1 and s2. Return a minimum number of times s1 has to be repeated such that s2 is a substring of it. If s2 can never be a substring then return -1.

Note: Both the strings contain only lowercase letters.

Examples:

Input: s1 = "ww", s2 = "www"
Output: 2
Explanation: Repeating s1 two times "wwww", s2 is a substring of it.

Input: s1 = "abcd", s2 = "cdabcdab" 
Output: 3 
Explanation: Repeating s1 three times "abcdabcdabcd", s2 is a substring of it. s2 is not a substring of s1 when it is repeated less than 3 times.

Input: s1 = "ab", s2 = "cab"
Output: -1
Explanation: No matter how many times we repeat s1, we can't get a string such that s2 is a substring of it.

Constraints:
1 ≤ s1.size(), s2.size() ≤ 105

'''
'''
def min_repeats_to_contain(s1, s2):
    # Minimum number of repetitions needed
    min_repeats = (len(s2) // len(s1)) + 1
    
    # Repeat s1 enough times to potentially contain s2
    repeated_s1 = s1 * min_repeats
    
    # Check if s2 is a substring
    if s2 in repeated_s1:
        return min_repeats
    
    # Check with one additional repetition
    repeated_s1 += s1
    if s2 in repeated_s1:
        return min_repeats + 1
    
    # If s2 is not found, return -1
    return -1

# Examples
print(min_repeats_to_contain("ww", "www"))         # Output: 2
print(min_repeats_to_contain("abcd", "cdabcdab")) # Output: 3
print(min_repeats_to_contain("ab", "cab"))        # Output: -1
'''


# Using KMP Method
def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix
    i = 1
    
    # Build the lps array
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Build the LPS (Longest Prefix Suffix) array for the pattern (s2)
    lps = build_lps(s2)
    
    i = 0  # index for s1
    j = 0  # index for s2
    
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        
        if j == m:
            return i - j  # found the match, return the starting index
        elif i < len(s1) and s1[i] != s2[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1  # if no match found

def min_repeats_to_contain(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    # Calculate the minimum number of times s1 needs to be repeated
    repeat_count = (len_s2 + len_s1 - 1) // len_s1  # ceiling division
    
    # Repeat the s1 at least repeat_count times
    repeated_s1 = s1 * repeat_count
    
    # Check if s2 is a substring of the repeated s1
    result = kmp_search(repeated_s1, s2)
    
    if result != -1:
        return repeat_count
    
    # Check if repeating once more time is enough
    repeated_s1 += s1
    result = kmp_search(repeated_s1, s2)
    
    if result != -1:
        return repeat_count + 1
    
    return -1  # if no repetition works, return -1

# Test cases
print(min_repeats_to_contain("ww", "www"))  # Output: 2
print(min_repeats_to_contain("abcd", "cdabcdab"))  # Output: 3
print(min_repeats_to_contain("ab", "cab"))  # Output: -1
print(min_repeats_to_contain("wwwwwwww", "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"))  # Output: 5


'''
Steps:

    Determine the Minimum Repetitions:
        If len(s2) > len(s1), then at least ceil(len(s2) / len(s1)) repetitions of s1 are needed to potentially contain s2.
        To account for the case where s2 starts at the end of one repetition of s1 and continues into the next, we might need one additional repetition.

    Construct the Repeated String:
        Repeat s1 the necessary number of times and check if s2 is a substring.

    Return Result:
        If s2 is found as a substring, return the number of repetitions.
        If not, return -1.

Explanation of Code:

    Calculate Minimum Repeats:
        Compute min_repeats=⌈len(s2)/len(s1)⌉min_repeats=⌈len(s2)/len(s1)⌉, which ensures the repeated s1 is at least as long as s2.

    Substring Check:
        First check if s2 is a substring of the repeated string with min_repeats.
        If not, check with one additional repetition to account for edge cases where s2 wraps around.

    Return the Result:
        If s2 is a substring, return the number of repetitions.
        Otherwise, return -1.

Complexity Analysis:

    Time Complexity:
        Constructing the repeated string: O(k⋅len(s1)), where k=min_repeats+1.
        Substring check: O(k⋅len(s1)) in the worst case.
        Overall: O(k⋅len(s1)), where k≈⌈len(s2)/len(s1)⌉+1

    Space Complexity:
        Space for the repeated string: O(k⋅len(s1)).
'''

'''
KMP Method
Steps to Implement the Solution with KMP:

    Understanding the Problem: We need to check the number of repetitions of s1 such that s2 is a substring of the repeated string. If s2 can't be formed as a substring of any number of repetitions of s1, we return -1.

    Using KMP: The KMP algorithm will help us efficiently search for the substring s2 within the repeated string s1.

    Optimal Approach:
        We will repeat s1 enough times so that the length of the resulting string is at least as long as s2.
        Instead of concatenating strings manually, we simulate the process of repeating s1 by adjusting the search window.
        Use KMP to search for s2 within this repeated string by simulating the process of matching s2 against the repeated s1.

Solution Approach:

    Simulate Repeated String: We don't actually repeat the string s1, but we treat it as if we are searching within a conceptually repeated s1.

    Use KMP Search: Search for s2 in the simulated repeated string by utilizing the KMP algorithm.

    KMP Algorithm:
        First, preprocess the pattern (s2) to create the prefix function (lps array).
        Use this function to efficiently search for s2 in the simulated repeated s1.
Explanation:

    KMP Search:
        The kmp_search function is used to search for s2 inside the repeated s1. It efficiently finds s2 inside s1 by utilizing the LPS (Longest Prefix Suffix) array that we built in the build_lps function.
    Repeat Calculation:
        We calculate how many times s1 must be repeated by checking the length of s2 and dividing it by the length of s1 (with ceiling division).
    Simulation of Repeated String:
        We simulate the repeated string by searching s2 inside the repeated s1. If s2 is found, we return the number of repetitions required.
        If not, we try one additional repetition and check again.

Time Complexity:

    Build LPS (Pattern Preprocessing): This takes O(m), where m is the length of s2.
    KMP Search: The search for s2 inside the repeated string s1 takes O(n + m), where n is the length of s1 and m is the length of s2.
    The total time complexity is therefore O(n + m) for the search part, plus the time to simulate repeating s1 (which is O(n) for a few repetitions).

Space Complexity:

    The space complexity is O(m) due to the LPS array used in the KMP algorithm.

'''