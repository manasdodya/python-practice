'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-bonus-problems/problem/square-root

Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.

    Floor value of any number is the greatest Integer which is less than or equal to that number

Examples:

Input: n = 4
Output: 2
Explanation: Since, 4 is a perfect square, so its square root is 2.

Input: n = 11
Output: 3
Explanation: Since, 11 is not a perfect square, floor of square root of 11 is 3.

Input: n = 1
Output: 1

Constraints:
1 ≤ n ≤  3 x 104

'''
def floor_sqrt(n):
    low, high = 1, n
    result = 1  # Default for n = 1

    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid

        if square == n:
            return mid  # Exact square root found
        elif square < n:
            result = mid  # Update potential result
            low = mid + 1
        else:
            high = mid - 1

    return result

# Test examples
examples = [4, 11, 1, 15, 30000]

for i, n in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: n = {n}")
    print(f"  Floor Sqrt: {floor_sqrt(n)}")
    print()

'''
Algorithm

    Initialization:
        Define the search range as low=1low=1 and high=nhigh=n.

    Binary Search:
        Calculate the mid-point of the current range: mid=low+(high−low)//2mid=low+(high−low)//2.
        Compute mid2mid2:
            If mid2==nmid2==n, then midmid is the exact square root, return midmid.
            If mid2<nmid2<n, update low=mid+1low=mid+1 and set the potential answer to midmid.
            If mid2>nmid2>n, update high=mid−1high=mid−1.

    Return Result:
        The result will be the last value of midmid for which mid2≤nmid2≤n.

Explanation of Example
Input:

    n=11n=11

    Binary Search:
        Initial range: low=1,high=11low=1,high=11
        Mid-point: mid=6,mid2=36>11mid=6,mid2=36>11, update high=5high=5.
        Mid-point: mid=3,mid2=9<11mid=3,mid2=9<11, update low=4low=4, result=3result=3.
        Mid-point: mid=4,mid2=16>11mid=4,mid2=16>11, update high=3high=3.

    Result:
        low>highlow>high, return result=3result=3.

Output:

    33

Complexity

    Time Complexity:
        O(log⁡n)O(logn), as the range is halved in each iteration.

    Space Complexity:
        O(1)O(1), as no extra space is used.

'''