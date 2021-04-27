class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]  # 树左侧的数量 * 树右侧的数量
        return dp[n]
        # C = 1
        # for i in range(n):
        #     C = C * 2 * (2 * i + 1) / (i + 2)
        # return int(C)
