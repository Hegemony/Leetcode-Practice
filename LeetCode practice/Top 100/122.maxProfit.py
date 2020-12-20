"""
股票：V1
"""


class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        minn = prices[0]
        dp = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            if prices[i] > minn:
                dp[i] = prices[i] - minn
            else:
                dp[i] = 0
            minn = min(prices[i], minn)
            print(dp, minn)
        return max(dp)


# print(Solution().maxProfit([7, 3, 4, 5, 6, 1, 2, 4]))
# print(Solution().maxProfit([7, 2, 4, 5, 6, 1, 2, 4]))


"""
股票：V2
做法一: 贪心
"""


class Solution2:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        dp = [0 for i in range(len(prices))]
        minn = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                dp[i] = prices[i] - minn
                minn = prices[i]
            else:
                minn = prices[i]
            # print(dp, minn)
        return sum(dp)


# print(Solution2().maxProfit([7, 1, 5, 3, 6, 4]))
# print(Solution2().maxProfit([1, 2, 3, 4, 5]))
"""
股票：V2
做法二: 动态规划
dp[i][0]      # 表示第i天未持有股票
dp[i][1]      # 表示第i天持有股票
dp[0][0] = 0  # 第0天没持有股票，说明没有花钱，手里的现金数为0, 一开始是没有钱的
dp[0][1] = -prices[i]  # 第0天持有股票，说明花钱了，手中现金数为-prices[i]
"""


class Solution2_2:
    def maxProfit(self, prices):
        l = len(prices)
        dp = [[0 for i in range(2)] for j in range(l)]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, l):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        print(dp)
        return dp[-1][0]


print(Solution2_2().maxProfit([7, 1, 5, 3, 6, 4]))
