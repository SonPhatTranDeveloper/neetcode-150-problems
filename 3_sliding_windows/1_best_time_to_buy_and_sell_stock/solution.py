"""
The key idea is holding two pointers, one for buy and one for selling

if selling point is higher than buying point:
    update the maximum profit
else
    update the buying point to the selling point

We update the selling point always
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Create two pointers
        left = 0
        right = 1

        # Keep track of the maximum profit
        max_profit = 0

        # Moving pointers
        while right < len(prices):
            # Check the prices at the pointers
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # If there is a better buying point
                left = right

            right += 1

        return max_profit
