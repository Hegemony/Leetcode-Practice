class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        n = len((grid[0]))
        cnt = 0

        def helper(i, j):
            grid[i][j] = '0'
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n:
                    if grid[newi][newj] == '1':
                        helper(newi, newj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':   # 一个岛屿递归一次
                    helper(i, j)
                    cnt += 1
        print(grid)
        return cnt


print(Solution().numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
