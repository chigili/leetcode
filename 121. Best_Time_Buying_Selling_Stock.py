import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxP = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else:
                buy = sell
            sell += 1
        return maxP


if __name__ == "__main__":
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
    sol = Solution()
    print(sol.maxProfit(nums))
