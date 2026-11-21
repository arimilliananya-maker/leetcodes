class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        single_day = prices[0]

        for i in range(1, len(prices)):
            dif_day = prices[i]

            if dif_day < single_day:
                single_day = dif_day
            else:
                profit = max(profit, dif_day - single_day)

        return profit