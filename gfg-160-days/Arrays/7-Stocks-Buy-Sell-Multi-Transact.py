'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/stock-buy-and-sell2615

The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

Examples:

Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 => 310 - 100 = 210. Buy the stock on day 4 and sell it on day 6 => 695 - 40 = 655. Maximum Profit = 210 + 655 = 865.

Input: prices[] = [4, 2, 2, 2, 4]
Output: 2
Explanation: Buy the stock on day 3 and sell it on day 4 => 4 - 2 = 2. Maximum Profit = 2.

Constraints:
1 <= prices.size() <= 105
0 <= prices[i] <= 104
'''

def maxProfit(prices):
    # Initialize profit as 0
    profit = 0
    
    # Traverse the price array from left to right
    for i in range(1, len(prices)):
        # If the current price is greater than the previous price, add the difference to profit
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    
    return profit

# Example usage
print(maxProfit([100, 180, 260, 310, 40, 535, 695]))  # Output: 865
print(maxProfit([4, 2, 2, 2, 4]))  # Output: 2


'''
Approach:

    Multiple Transactions:
        We can buy and sell the stock on multiple days.
        We are only interested in profit, which is calculated by finding the difference between buying and selling price. This means we should try to take advantage of every price increase.

    Greedy Strategy:
        The key observation here is that to maximize profit, we should buy when the price is increasing (or when there is a price difference) and sell immediately after it increases.
        For every consecutive pair of days where the price increases (i.e., price[i] < price[i+1]), we should "buy" on day i and "sell" on day i+1 because the profit is guaranteed to be positive.

    Algorithm:
        Traverse the price array from left to right.
        If the price on the next day (price[i+1]) is higher than the price on the current day (price[i]), we consider it as a profitable transaction and add the difference price[i+1] - price[i] to the total profit.

    Time Complexity:
        We only need to iterate through the array once, so the time complexity is O(n), where nn is the number of days (or the size of the array).

    Space Complexity:
        We use a constant amount of space (just an accumulator for the profit), so the space complexity is O(1).
    
Explanation:

    First Example: [100, 180, 260, 310, 40, 535, 695]
        Transaction 1: Buy on day 0 at price 100, sell on day 3 at price 310. Profit: 310 - 100 = 210.
        Transaction 2: Buy on day 4 at price 40, sell on day 6 at price 695. Profit: 695 - 40 = 655.
        Total Profit: 210 + 655 = 865.

    Second Example: [4, 2, 2, 2, 4]
        Transaction 1: Buy on day 3 at price 2, sell on day 4 at price 4. Profit: 4 - 2 = 2.
        Total Profit: 2.

Time and Space Complexity:

    Time Complexity: O(n)O(n), where n is the number of days (or the length of the array). We are iterating through the array once.
    Space Complexity: O(1)O(1), because we are only using a single variable to accumulate the profit.

Edge Cases:

    Array with no price change (e.g., [1, 1, 1, 1, 1]):
        No transactions will be made, and the total profit will be 0.
    Array with all decreasing prices (e.g., [5, 4, 3, 2, 1]):
        No profit can be made, and the total profit will be 0.
    Array with a single element (e.g., [10]):
        No transactions can be made, and the total profit will be 0.
'''