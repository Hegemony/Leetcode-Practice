class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minn = prices[0]
        dp = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            if prices[i] - minn > 0:
                dp[i] = prices[i] - minn
            else:
                dp[i] = 0
            minn = min(prices[i], minn)
        return max(dp)