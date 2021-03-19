class Solution:
    def maxValue(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


print(Solution().maxValue([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
