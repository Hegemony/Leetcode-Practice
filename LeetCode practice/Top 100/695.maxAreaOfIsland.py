class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if not grid:
            return 0

        def dfs(i, j):
            if grid[i][j] == 1:
                res.add((i, j))
                for di, dj in directions:
                    newi, newj = i + di, j + dj
                    if 0 <= newi < n and 0 <= newj < m and (newi, newj) not in res:
                        dfs(newi, newj)
                # res.remove((i, j))

        res = set()
        maxx = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in res:
                    oldl = len(res)  # 集合中存的之前的面积
                    dfs(i, j)
                    cnt += 1  # 岛屿数量
                    newl = len(res)  # 计算完新的岛屿后得到的面积
                    maxx = max(maxx, newl - oldl)  # 差值为新增的这个岛屿带来的面积
        return maxx


print(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
print(Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
