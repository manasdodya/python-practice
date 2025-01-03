'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/allocate-minimum-number-of-pages0937

You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

    Each student receives atleast one book.
    Each student is assigned a contiguous sequence of books.
    No book is assigned to more than one student.

The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Allocation can be done in following ways:
[12] and [34, 67, 90] Maximum Pages = 191
[12, 34] and [67, 90] Maximum Pages = 157
[12, 34, 67] and [90] Maximum Pages = 113.
Therefore, the minimum of these cases is 113, which is selected as the output.

Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Allocation can not be done.

Input: arr[] = [22, 23, 67], k = 1
Output: 112

Constraints:
1 <=  arr.size() <= 106
1 <= arr[i] <= 103
1 <= k <= 103 

'''

def is_feasible(arr, n, k, max_pages):
    students_required = 1
    current_pages = 0

    for pages in arr:
        if current_pages + pages > max_pages:
            # Assign books to a new student
            students_required += 1
            current_pages = pages
            if students_required > k:
                return False
        else:
            current_pages += pages

    return True

def allocate_books(arr, k):
    n = len(arr)
    if k > n:
        return -1

    # Set search space for binary search
    low, high = max(arr), sum(arr)
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if is_feasible(arr, n, k, mid):
            result = mid
            high = mid - 1  # Try to minimize maximum pages further
        else:
            low = mid + 1  # Increase max_pages limit

    return result

# Test examples
examples = [
    ([12, 34, 67, 90], 2),
    ([15, 17, 20], 5),
    ([22, 23, 67], 1),
]

for i, (arr, k) in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: arr={arr}, k={k}")
    print(f"  Output: {allocate_books(arr, k)}")
    print()

'''
Approach

    Determine Bounds:
        The smallest possible maximum pages is the maximum number of pages in any single book (max(arr)).
        The largest possible maximum pages is the sum of all book pages (sum(arr)).

    Binary Search on the Maximum Pages:
        Use binary search to find the minimum "maximum pages" that can be allocated.
        Let low be max(arr) and high be ∑(arr)∑(arr).
        Check for feasibility of mid-point as the maximum page allocation.

    Feasibility Check:
        Use a helper function to check if it is possible to allocate books to kk students such that no student gets more than midmid pages.
        If allocation is possible, try for a smaller maximum by reducing high.
        Otherwise, increase low.

    Result:
        The smallest feasible midmid is the answer.
        Return -1 if k>len(arr).

Explanation of Example
Input: arr = [12, 34, 67, 90], k = 2

    Bounds:
        low=max(arr)=90
        high=∑(arr)=203.

    Binary Search:
        mid=(90+203)//2=146.
        Check feasibility with text{max_pages} = 146:
            Allocate [12, 34] to Student 1, [67, 90] to Student 2.
            Feasible. Update result=146, high=145.
        mid=(90+145)//2=117.
        Check feasibility:
            Allocate [12, 34] to Student 1, [67] to Student 2, [90] to Student 3.
            Not feasible. Increase low=118low=118.
        Repeat until low=113, high=112.

    Result:
        The smallest feasible text{max_pages} is 113113.

Complexity Analysis

    Time Complexity:
        Binary Search: O(log(sum(arr) - max(arr))).
        Feasibility Check: O(n).
        Total: O(nlog(sum(arr) - max(arr))).

    Space Complexity:
        O(1), as no additional data structures are used.
'''