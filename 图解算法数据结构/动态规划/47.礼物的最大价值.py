class Solution:
    def maxValue(self, grid) -> int:
        m = len(grid)  # m行
        n = len(grid[0])  # n列
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                if i == 0 and j != 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                if j == 0 and i != 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                if i != 0 and j != 0:
                    dp[i][j] = max(grid[i][j] + dp[i][j-1], grid[i][j] + dp[i-1][j])
                    print(dp)
        return dp[-1][-1]

print(Solution().maxValue([[1, 3, 1],
                           [1, 5, 1],
                           [4, 2, 1]]))

# print(Solution().maxValue([[1, 3, 1],
#                            [1, 5, 1],
#                            [8, 2, 1]]))

"""
题解：
直接在原数组上修改
设 f(i, j)为从棋盘左上角走至单元格 (i ,j)的礼物最大累计价值，易得到以下递推关系：f(i,j) 等于 f(i,j-1)和 f(i-1,j)
中的较大值加上当前单元格礼物价值 grid(i,j) 。
f(i,j)=max[f(i,j−1),f(i−1,j)]+grid(i,j)

因此，可用动态规划解决此问题，以上公式便为转移方程。

"""
class Solution1:
    def maxValue(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        print(grid)
        return grid[-1][-1]

print(Solution1().maxValue([[1, 3, 1],
                           [1, 5, 1],
                           [4, 2, 1]]))