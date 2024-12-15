'''
URL: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2

Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.

Examples:

Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.

Input: prices[] = [7, 6, 4, 3, 1]
Output: 0 
Explanation: Here the prices are in decreasing order, hence if we buy any day then we cannot sell it at a greater price. Hence, the answer is 0.

Input: prices[] = [1, 3, 6, 9, 11]
Output: 10 
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1].

Constraint:
1 <= prices.size()<= 105
0 <= prices[i] <=104
'''

def maxProfit(prices):
    # Initialize variables for minimum price and maximum profit
    min_price = float('inf')
    max_profit = 0
    
    # Traverse through the price list
    for price in prices:
        # Update the minimum price
        min_price = min(min_price, price)

        # Calculate the potential profit if selling at the current price
        max_profit = max(max_profit, price - min_price) 
    
    return max_profit

# Example usage
print(maxProfit([7, 10, 1, 3, 6, 9, 2]))  # Output: 8
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0
print(maxProfit([1, 3, 6, 9, 11]))  # Output: 10

'''
Algorithm:

    Initialize:
        min_price = first price in array.
        max_profit = 0 (initially no profit).

    Traverse the price array:
        For each price, check if it is less than min_price. If so, update min_price.
        Otherwise, calculate the profit by subtracting min_price from the current price, and update max_profit if this profit is greater than the current max_profit.

    Return the max_profit, which will either be the maximum profit or 0 if no profit is possible.

Explanation:

    First Example: [7, 10, 1, 3, 6, 9, 2]
        Buy on day 2 (price = 1) and sell on day 5 (price = 9). Profit = 9 - 1 = 8.

    Second Example: [7, 6, 4, 3, 1]
        The prices are strictly decreasing, so no opportunity for profit. Return 0.

    Third Example: [1, 3, 6, 9, 11]
        The prices are strictly increasing, so buy on day 0 (price = 1) and sell on day 4 (price = 11). Profit = 11 - 1 = 10.

Time Complexity:

    Time Complexity: O(n), where nn is the length of the prices array. We only traverse the array once.
    Space Complexity: O(1), since we are only using a constant amount of space to store the min_price and max_profit.
'''