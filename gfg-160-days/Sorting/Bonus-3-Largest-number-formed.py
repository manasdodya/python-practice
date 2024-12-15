'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-bonus-problems/problem/largest-number-formed-from-an-array1117

Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

Examples:

Input: arr[] = [3, 30, 34, 5, 9]
Output: "9534330"
Explanation: Given numbers are [3, 30, 34, 5, 9], the arrangement "9534330" gives the largest value.

Input: arr[] = [54, 546, 548, 60]
Output: "6054854654"
Explanation: Given numbers are [54, 546, 548, 60], the arrangement "6054854654" gives the largest value.

Input: arr[] = [3, 4, 6, 5, 9]
Output: "96543"
Explanation: Given numbers are [3, 4, 6, 5, 9], the arrangement "96543" gives the largest value.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105

'''

from functools import cmp_to_key

def largestNumber(arr):
    # Custom comparator to decide order based on concatenation
    def compare(x, y):
        if x + y > y + x:
            return -1  # x should come before y
        elif x + y < y + x:
            return 1   # y should come before x
        else:
            return 0   # x and y are equal in order

    # Convert integers to strings
    arr = list(map(str, arr))

    # Sort using the custom comparator
    arr.sort(key=cmp_to_key(compare))

    # Edge case: If the largest number is "0", the result is "0"
    if arr[0] == "0":
        return "0"

    # Join the sorted numbers to form the largest number
    return ''.join(arr)


# Example Usage
if __name__ == "__main__":
    arr1 = [3, 30, 34, 5, 9]
    print(largestNumber(arr1))  # Output: "9534330"

    arr2 = [54, 546, 548, 60]
    print(largestNumber(arr2))  # Output: "6054854654"

    arr3 = [3, 4, 6, 5, 9]
    print(largestNumber(arr3))  # Output: "96543"

    arr4 = [0, 0, 0]
    print(largestNumber(arr4))  # Output: "0"

'''
Algorithm:
    Custom Comparator for Sorting:
    Sort the integers based on the comparison of their string concatenations.
    For two strings x and y, if x+y>y+x, x should come before y.

    Sorting the Numbers:
    Convert all integers to strings.
    Sort the strings using the custom comparator.

    Handle Edge Cases:
    If the array contains only zeros (e.g., [0,0,0][0,0,0]), return "0".

    Concatenate the Numbers:
    Concatenate the sorted numbers to form the result.

Explanation of the Comparator

    For two numbers x="54"x="54" and y="546"y="546":
        Concatenate in both orders: x+y="54546", y+x="54654".
        Since y+x>x+y, y should come before x.

    This custom rule ensures the numbers are sorted in the order that maximizes the concatenated result.

Complexity Analysis

    Time Complexity:
        Sorting: O(nlogn), where nn is the number of elements in the array.
        Custom comparator involves string concatenation, which takes O(k), where k is the average number of digits per number. 
        Thus, the total time complexity is O(nlogn⋅k).
        

    Space Complexity:
        Converting integers to strings requires O(n⋅k) space.
        Sorting is done in-place, so no additional space is needed for sorting.
'''