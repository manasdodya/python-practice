'''
URL : https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-bonus-problems/problem/minimum-days-to-make-m-bouquets

You have a row of flowers, where each flower blooms after a specific day. The array arr represents the blooming schedule: arr[i] is the day the flower at position i will bloom. To create a bouquet, you need to collect k adjacent bloomed flowers. Each flower can only be used in one bouquet.

Your goal is to find the minimum number of days required to make exactly m bouquets. If it is not possible to make m bouquets with the given arrangement, return -1.
Examples:

Input: m = 3, k = 2, arr[] = [3, 4, 2, 7, 13, 8, 5]
Output: 8
Explanation: We need 3 bouquets and each bouquet should have 2 flowers. After day 8: [x, x, x, x, _, x, x], we can make first bouquet from the first 2 flowers, second bouquet from the next 2 flowers and the third bouquet from the last 2 flowers.

Input: m = 2, k = 3, arr[] = [5, 5, 5, 5, 10, 5, 5]
Output: 10
Explanation: We need 2 bouquets and each bouquet should have 3 flowers, After day 5: [x, x, x, x, _, x, x], we can make one bouquet of the first three flowers that bloomed, but cannot make another bouquet. After day 10: [x, x, x, x, x, x, x], Now we can make two bouquets, taking 3 adjacent flowers in one bouquet.

Input: m = 3, k = 2, arr[] = [1, 10, 3, 10, 2]
Output: -1
Explanation: As 3 bouquets each having 2 flowers are needed, that means we need 6 flowers. But there are only 5 flowers so it is impossible to get the needed bouquets therefore -1 will be returned.

Constraints:
1 <= k <= arr.size() <= 105
1 <= m <= 105
1 <= arr[i] <= 109


'''
def min_days_to_make_bouquets(arr, m, k):
    # Helper function to check if m bouquets can be made by day "day"
    def can_make_bouquets(day):
        bouquets = 0
        flowers = 0
        for bloom_day in arr:
            if bloom_day <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
            if bouquets >= m:  # Early exit if enough bouquets are formed
                return True
        return bouquets >= m

    # Edge case: If there are not enough flowers to make m bouquets
    if len(arr) < m * k:
        return -1

    low, high = min(arr), max(arr)
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if can_make_bouquets(mid):
            result = mid  # Update result to current feasible day
            high = mid - 1  # Try for earlier days
        else:
            low = mid + 1  # Try for later days

    return result

# Test examples
examples = [
    (3, 2, [3, 4, 2, 7, 13, 8, 5]),
    (2, 3, [5, 5, 5, 5, 10, 5, 5]),
    (3, 2, [1, 10, 3, 10, 2]),
]

for i, (m, k, arr) in enumerate(examples):
    print(f"Example {i+1}:")
    print(f"  Input: m = {m}, k = {k}, arr = {arr}")
    print(f"  Minimum days: {min_days_to_make_bouquets(arr, m, k)}")
    print()


'''
Algorithm

    Define Search Range:
        low=min⁡(arr)low=min(arr): The earliest blooming day.
        high=max⁡(arr)high=max(arr): The latest blooming day.

    Binary Search:
        Calculate mid=low+(high−low)//2mid=low+(high−low)//2.
        Use a helper function to check if mm bouquets, each of size kk, can be made by day midmid.
        If it is possible, update high=mid−1high=mid−1 to try fewer days.
        Otherwise, update low=mid+1low=mid+1 to allow more days.

    Helper Function: CanMakeBouquets(day, arr, m, k):
        Count consecutive flowers that have bloomed by day dayday.
        Whenever kk consecutive flowers are found, increment the bouquet count and reset the consecutive flower count.
        If mm bouquets are formed before finishing the array, return True.
        If the loop completes without forming mm bouquets, return False.

    Return Result:
        After the binary search, lowlow will contain the minimum number of days required, or return -1 if low>highlow>high.


Explanation of Example
Input:

    m=3,k=2,arr=[3,4,2,7,13,8,5]

    Binary Search:
        Initial range: low=2,high=13low=2,high=13.
        Check mid=7: Possible bouquets: 2 (not sufficient). Update low=8.
        Check mid=10: Possible bouquets: 3 (sufficient). Update high=9.
        Check mid=8: Possible bouquets: 3 (sufficient). Update high=7.

    Result:
        Minimum days: 8.

Output:

    8

Complexity

    Time Complexity:
        Binary search: O(log(max(arr)−min(arr))).
        Feasibility check: O(n) for each mid.
        Total: O(n⋅log(max(arr))).

    Space Complexity:
        O(1), no additional data structures are used.

'''