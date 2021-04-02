class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        minn = float('inf')
        dp = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            minn = min(minn, prices[i - 1])
            dp[i] = max(dp[i - 1], prices[i] - minn)
        return dp[-1]

