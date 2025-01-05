'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/print-anagrams-together

Given an array of strings, return all groups of strings that are anagrams. 
The strings in each group must be arranged in the order of their appearance in the original array. 
Refer to the sample case for clarification.

Examples:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.

Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.

Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]
Explanation: 
Group 1: "abc", "bac", and "cab" are anagrams.
Group 2: "listen", "silent", and "enlist" are anagrams.
Group 3: "rat", "tar", and "art" are anagrams.

Constraints:
1<= arr.size() <=100
1<= arr[i].size() <=10
'''

def groupAnagrams(arr):
    # Initialize an empty dictionary to store groups of anagrams
    anagram_groups = {}

    # Iterate over each word in the input list
    for word in arr:
        # Create a frequency count for the current word (size 26 for lowercase English letters)
        count = [0] * 26
        
        # Fill the frequency array with the counts of each character in the word
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        # Convert the count array to a tuple (hashable) to use it as a dictionary key
        count_tuple = tuple(count)
        
        # If the key doesn't exist in the dictionary, initialize it with an empty list
        if count_tuple not in anagram_groups:
            anagram_groups[count_tuple] = []
        
        # Append the original word to the corresponding anagram group
        anagram_groups[count_tuple].append(word)

    # Return the list of anagram groups (dictionary values)
    return list(anagram_groups.values())

arr = ["act", "god", "cat", "dog", "tac"]
print(groupAnagrams(arr))
arr = ["no", "on", "is"]
print(groupAnagrams(arr))
arr = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
print(groupAnagrams(arr))

'''
Approach

    Signature creation: For each string, create a tuple of size 26 (one entry for each character in the English alphabet). The index in this tuple corresponds to the letter (e.g., index 0 for 'a', index 1 for 'b', etc.), and the value at each index corresponds to the frequency of that character in the string.
    Hashing: Use this tuple as a key in a dictionary to group all anagrams together. Anagrams will have the same signature.
    Final result: The dictionary values will contain the anagram groups.

Algorithm

    Initialize an empty dictionary to store the anagram groups.
    For each string:
        Create a frequency count tuple of length 26.
        Use this tuple as the key in the dictionary.
        Append the original string to the list corresponding to that key.
    Return all values (the anagram groups).


Time Complexity

    Time Complexity: The time complexity is O(n⋅m), where:
        n is the number of strings in the input array.
        m is the average length of the strings.
        This is because for each string, we iterate through all its characters to create the frequency count, which takes O(m) time, and inserting or updating a dictionary entry takes constant time.
    Space Complexity: The space complexity is O(n⋅m), because we are storing the frequency count tuple for each string in the dictionary, and each string appears once in the result.

    
Explanation of the Code

    Frequency Count: For each string, we initialize a list of size 26 (count) to track the frequency of each letter (from 'a' to 'z'). For each character in the string, we calculate its corresponding index by subtracting the ASCII value of 'a' from the ASCII value of the character.

    Tuple as Key: The count list is converted to a tuple (count_tuple) so that it can be used as a key in the dictionary. Tuples are immutable and hashable, making them suitable for use as dictionary keys.

    Dictionary Usage: The dictionary anagram_groups uses the count_tuple as a key and appends the string to the list of anagrams associated with that key.

    Final Result: After processing all strings, we return the list of values from the dictionary, which contains all the anagram groups.

Examples
Example 1:

Input:

arr = ["act", "god", "cat", "dog", "tac"]

Execution:

    For "act", the frequency count tuple is (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0).
    For "god", the frequency count tuple is (1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0).
    Both "act", "cat", and "tac" share the same tuple, as do "god" and "dog".
    Final output:

    [["act", "cat", "tac"], ["god", "dog"]]

Example 2:

Input:

arr = ["no", "on", "is"]

Execution:

    "no" and "on" have the same frequency count tuple.
    "is" has a different tuple.
    Final output:

[["no", "on"], ["is"]]
'''