'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/find-h-index--165609

Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith paper. The task is to find the H-index.

    H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times.

Examples:

Input: citations[] = [3, 0, 5, 3, 0]
Output: 3
Explanation: There are at least 3 papers (3, 5, 3) with at least 3 citations.

Input: citations[] = [5, 1, 2, 4, 1]
Output: 2
Explanation: There are 3 papers (with citation counts of 5, 2, and 4) that have 2 or more citations. However, the H-Index cannot be 3 because there aren't 3 papers with 3 or more citations.

Input: citations[] = [0, 0]
Output: 0

Constraints:
1 ≤ citations.size() ≤ 106
0 ≤ citations[i] ≤ 106

'''
def h_index(citations):
    n = len(citations)
    # Create a frequency array
    count = [0] * (n + 1)
    
    # Populate the frequency array
    for citation in citations:
        if citation >= n:
            count[n] += 1
        else:
            count[citation] += 1
    
    # Traverse from right to left to calculate cumulative sum
    cumulative_papers = 0
    for h in range(n, -1, -1):
        cumulative_papers += count[h]
        # Check if the current h satisfies the H-Index condition
        if cumulative_papers >= h:
            return h
    
    return 0  # Default case if no H-Index is found

print(h_index([3, 0, 5, 3, 0])) # Output = 3
print(h_index([5, 1, 2, 4, 1])) # Output = 2
print(h_index([0, 0])) # Output = 0


'''
Algorithm:

    Counting Citations:
        Create a frequency array count of size n+1n+1, where nn is the number of papers.
        Count how many papers have each citation count. If a paper has citations greater than nn, count it in count[n].

    Cumulative Sum:
        Traverse the count array from right to left to calculate the cumulative sum. This gives the number of papers with at least a certain citation count.

    Find H-Index:
        The H-Index is the largest value hh such that the number of papers with at least hh citations is ≥h.

Explanation:
Example 1:

Input: citations = [3, 0, 5, 3, 0]

    Frequency Array:
    count=[2,0,0,2,0,1]
    count=[2,0,0,2,0,1]
        2 papers have 0 citations.
        0 papers have 1 citation.
        2 papers have 3 citations.
        1 paper has 5 citations (counted in count[5]).

    Cumulative Papers: Traverse from right to left:
        h=5,cumulative_papers=1h=5,cumulative_papers=1
        h=4,cumulative_papers=1h=4,cumulative_papers=1
        h=3,cumulative_papers=3h=3,cumulative_papers=3 (Stop, since cumulative_papers≥hcumulative_papers≥h).

Output: 3
Example 2:

Input: citations = [5, 1, 2, 4, 1]

    Frequency Array:
    count=[0,2,1,0,1,1]
    count=[0,2,1,0,1,1]

    Cumulative Papers:
        h=5,cumulative_papers=1h=5,cumulative_papers=1
        h=4,cumulative_papers=2h=4,cumulative_papers=2
        h=3,cumulative_papers=2h=3,cumulative_papers=2
        h=2,cumulative_papers=4h=2,cumulative_papers=4 (Stop, since cumulative_papers≥hcumulative_papers≥h).

Output: 2
Complexity:

    Time Complexity: O(n) for building the frequency array and cumulative sum traversal.
    Space Complexity: O(n) for the frequency array.
    
'''