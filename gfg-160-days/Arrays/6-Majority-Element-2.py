'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote

You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

Examples:

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.

Input: arr[] = [1, 2, 3, 4, 5]
Output: []
Explanation: no candidate occur more than n/3 times.

Constraint:
1 <= arr.size() <= 106
-109 <= arr[i] <= 109
'''

def majorityElement(arr):
    n = len(arr)
    if n == 0:
        return []
    
    # Step 1: Find the two potential majority candidates
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0
    
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    
    # Step 2: Verify the candidates
    count1, count2 = 0, 0
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    
    result = []
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)
    
    # Return result sorted
    return sorted(result)

# Example usage
print(majorityElement([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))  # Output: [5, 6]
print(majorityElement([1, 2, 3, 4, 5]))                    # Output: []


'''
To solve this problem where we need to find candidates with more than one-third of the total votes in the array, we can use Boyer-Moore Voting Algorithm extended for multiple majority elements.
Problem Breakdown:

    We need to find all candidates whose occurrences are greater than n/3n/3, where nn is the size of the array.
    If there are no candidates with more than n/3n/3 votes, return an empty array.
    The answer should be returned in increasing order.

Approach:

    Boyer-Moore Voting Algorithm for Majority Elements:
        The classical Boyer-Moore algorithm is designed for a single majority element (which appears more than n/2n/2 times).
        For this problem, we need to find elements that appear more than n/3n/3 times. This requires a modified version of the algorithm to handle multiple potential candidates (at most 2).

    Modified Algorithm:
        We maintain two potential candidates and their counts.
        First, we scan the array and find two potential candidates (candidate1 and candidate2), counting how many times each appears.
        Then, we verify if these candidates really appear more than n/3n/3 times by performing a second pass over the array to count their actual occurrences.

    Steps:
        First pass: Identify two candidates using two counters.
        Second pass: Count the actual occurrences of these candidates to check if they are greater than n/3n/3.

    Edge Case:
        If no candidates exceed n/3n/3 occurrences, return an empty array.

Algorithm:

    Find Two Potential Candidates:
        Traverse the array to find two candidates, where each candidate could potentially appear more than n/3n/3 times.

    Validate Candidates:
        Traverse the array again to count the actual occurrences of the candidates.

    Return Results:
        If any of the candidates appear more than n/3n/3 times, add them to the result and return the sorted list.

Explanation:

    First Pass (Find Potential Candidates):
        Iterate over the array and maintain two potential candidates (candidate1 and candidate2) and their respective counts (count1 and count2).
        If count1 or count2 is zero, assign the current element as a new candidate and set the count to 1.
        If the current element is equal to one of the candidates, increment the corresponding count.
        If both counts are non-zero and the current element is not equal to either candidate, decrement both counts.

    Second Pass (Count Occurrences):
        Traverse the array again to count how many times candidate1 and candidate2 appear.
        If a candidate appears more than n/3n/3 times, it is a valid majority element.

    Sorting:
        The result is sorted to return the answer in increasing order, as required.

Time Complexity:

    Time Complexity: O(n)O(n) because we only traverse the array twice — once to find potential candidates and once to validate their occurrences.
    Space Complexity: O(1)O(1) because we are using only a few variables to store candidates and counts, which does not depend on the size of the input.

Example Walkthrough:

    Input: [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
        First pass: The potential candidates are 5 and 6 with counts 4 and 5 respectively.
        Second pass: The actual counts are verified and both 5 and 6 appear more than n/3=3.67n/3=3.67 times, so both are added to the result.
        Output: [5, 6].

    Input: [1, 2, 3, 4, 5]
        First pass: No candidate exceeds one-third of the array size.
        Second pass: None of the candidates exceed n/3=1.67n/3=1.67 times.
        Output: [].

'''