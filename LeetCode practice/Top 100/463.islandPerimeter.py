class Solution:
    def islandPerimeter(self, grid) -> int:
        """
        直接遍历，如果当前值为1，加4（四条边），如果左边有1，减2（两条边重合），上面有1，减2。
        最后相加即可
        :param grid:
        :return:
        """
        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += 4
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        res -= 2
        return res
