"""
题解：动态规划
dp(i, j)表示以（i， j）为右下角，且只包含1的正方形
（1）如果该位置的值是 0，则 dp(i, j) = 0，因为当前位置不可能在由 1组成的正方形中；

（2）如果该位置的值是 1，则 dp(i, j) 的值由其上方、左方和左上方的三个相邻位置的 dp值决定。
"""


class Solution:
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return 0
        maxSide = 0
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide ** 2
