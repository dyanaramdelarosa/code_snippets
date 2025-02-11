# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Author: Dyanara Dela Rosa
# Date: Feb 11, 2025


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute-force
        # max_profit = 0
        # prices_len = len(prices)
        # for x in range(0, prices_len - 1):
        #     for y in range(x, prices_len):
        #         max_profit = max(prices[y] - prices[x], max_profit)

        # return max_profit

        max_profit, buy, sell = 0, 0, 1

        while sell < len(prices):
            max_profit = max(prices[sell] - prices[buy], max_profit)

            if prices[sell] < prices[buy]:
                buy = sell
            else:
                sell = sell + 1

        return max_profit
