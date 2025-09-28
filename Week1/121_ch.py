from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        min_buy_price = prices[0]
        
        for idx in range(1, len(prices)):
            