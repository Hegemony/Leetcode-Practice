class Solution:
    def numIslands(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        if not grid:
            return 0
        cnt = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = set()

        def dfs(i, j):
            if grid[i][j] == '1':
                res.add((i, j))
                for di, dj in directions:
                    newi, newj = i + di, j + dj
                    if 0 <= newi < m and 0 <= newj < n and (newi, newj) not in res:
                        dfs(newi, newj)
                # res.remove((i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in res:
                    dfs(i, j)
                    cnt += 1  # 求岛屿数量
                    print(cnt)
        return cnt


print(Solution().numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]]))
