"""
dp[i][0]     # 表示目前持有一只股票
dp[i][1]     # 表示目前不持有股票，且处于冷冻期 如果第 i 天结束之后处于冷冻期，那么第 i+1天无法买入股票。
dp[i][2]     # 目前不持有股票，且不处于冷冻期
"""


class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        l = len(prices)
        dp = [[0 for i in range(3)] for i in range(l)]
        dp[0][0], dp[0][1], dp[0][2] = -prices[0], 0, 0
        for i in range(1, l):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])  # 比较(第i-1天手里也有股票, 和第i-1天没有股票但不是冷冻期)
            dp[i][1] = dp[i - 1][0] + prices[i]  # 第i + 1天是冷冻期，所以第i-1天有股票并且在第i天卖掉
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])  # 比较(第i-1天是冷冻期, 和第i-1天没有股票但不是冷冻期)
        return max(dp[l - 1][1], dp[l - 1][2])


"""
dp[i][0] # 表示第i天不持股
dp[i][1] # 表示第i天持股
"""


class Solution1:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        l = len(prices)
        if l < 2:
            return 0
        dp = [[0 for i in range(2)] for i in range(l)]
        dp[0][0] = 0  # 第0天不持股,所以为0
        dp[0][1] = -prices[0]  # 第0天持股，价格为-prices[0]
        # 第1天不持股, 要么第0天不持股，要么第0天持股，然后第一天卖出
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        # 第1天持股, 要么第0天持股，要么第0天不持股，然后第0天不持股第1天持股
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])

        for i in range(2, l):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])  # i - 1天作为冷冻期
        return dp[-1][0]