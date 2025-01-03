'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-bonus-problems/problem/koko-eating-bananas

Given an array arr[] of integers where each element represents a pile of bananas, and Koko has k hours to finish all the piles, find the minimum number of bananas (s) Koko must eat per hour to finish all the bananas within k hours. Each hour, Koko chooses a pile and eats s bananas from it. If the pile has fewer than s bananas, she consumes the entire pile for that hour and won't eat any other banana during that hour.

Examples:

Input: arr[] = [3, 6, 7, 11] , k = 8
Output: 4
Explanation: Koko eats at least 4 bananas per hour to finish all piles within 8 hours, as she can consume each pile in 1 + 2 + 2 + 3 = 8 hours.

Input: arr[] = [30, 11, 23, 4, 20], k = 5
Output: 30
Explanation: With 30 bananas per hour, Koko completes each pile in 1 hour, totaling 5 hours, which matches k = 5.

Input: arr[] = [5, 10, 15, 20], k = 7
Output: 10
Explanation: At 10 bananas per hour, Koko finishes in 7 hours, just within the k = 7 limit.

Constraint:
1 <= arr.size() <= 105 
1 <= arr[i] <= 104
arr.size() <= k <= 2*105

'''

def min_eating_speed(arr, k):
    def is_feasible(speed):
        hours = 0
        for pile in arr:
            hours += (pile + speed - 1) // speed  # Equivalent to ceil(pile / speed)
        return hours <= k

    low, high = 1, max(arr)
    result = high

    while low <= high:
        mid = low + (high - low) // 2
        if is_feasible(mid):
            result = mid  # Update result to the current feasible speed
            high = mid - 1
        else:
            low = mid + 1

    return result

# Test examples
examples = [
    ([3, 6, 7, 11], 8),
    ([30, 11, 23, 4, 20], 5),
    ([5, 10, 15, 20], 7),
]

for i, (arr, k) in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: arr = {arr}, k = {k}")
    print(f"  Minimum speed: {min_eating_speed(arr, k)}")
    print()


'''
Algorithm

    Define Search Range:
        low=1low=1: Minimum possible bananas per hour.
        high=max⁡(arr)high=max(arr): Maximum bananas per hour (eating an entire largest pile in one hour).

    Binary Search:
        Calculate mid=low+(high−low)//2mid=low+(high−low)//2.
        Check if Koko can eat all the bananas within kk hours at speed midmid using a helper function.
        If she can, try a smaller speed by updating high=mid−1high=mid−1.
        Otherwise, increase the speed by updating low=mid+1low=mid+1.

    Helper Function: IsFeasible(speed, arr, k):
        For each pile in arrarr, calculate the number of hours needed to finish it:
        hours=⌈pilespeed⌉
        hours=⌈speedpile​⌉ This can be implemented as hours=(pile+speed−1)//speedhours=(pile+speed−1)//speed.
        Sum these hours for all piles and check if the total is ≤k≤k.

    Return Result:
        After the binary search ends, lowlow will contain the minimum speed.

Explanation of Example
Input:

    arr=[3,6,7,11],k=8arr=[3,6,7,11],k=8

    Binary Search:
        Initial range: low=1,high=11low=1,high=11.
        Check mid=6mid=6: hours=1+1+2+2=6≤8hours=1+1+2+2=6≤8, feasible. Update high=5high=5.
        Check mid=3mid=3: hours=1+2+3+4=10>8hours=1+2+3+4=10>8, not feasible. Update low=4low=4.
        Check mid=4mid=4: hours=1+2+2+3=8≤8hours=1+2+2+3=8≤8, feasible. Update high=3high=3.

    Result:
        Minimum speed is 4.

Output:
    4

Complexity

    Time Complexity:
        Binary search: O(log(max(arr))).
        Feasibility check: O(n) for each mid.
        Total: O(n⋅log(max(arr))).

    Space Complexity:
        O(1), no additional data structures are used.

'''