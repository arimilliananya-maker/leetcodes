class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count=0
        for i in range(len(costs)):
            if costs[i]<=coins:
                coins=coins-costs[i]
                count+=1
        return count