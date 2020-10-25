class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [0 for i in range(n)]
        minn = prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i] - minn)
            minn = min(minn, prices[i])
        return dp[-1]