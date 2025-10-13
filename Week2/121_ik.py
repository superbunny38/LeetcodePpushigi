from typing import List


class Solution:
    # Greedy
    # Time: O(n)
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(price - min_price, profit)
        return profit
    # Brute Force
    # Time: O(n^2)
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit
