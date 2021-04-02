class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        temp = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > temp:
               res += prices[i] - temp
            temp = prices[i]
        return res


