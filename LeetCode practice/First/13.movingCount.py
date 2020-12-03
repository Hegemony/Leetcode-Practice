class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        board = [[0 for i in range(n)] for j in range(m)]
        visited = set()
        for i in range(m):
            res1 = i // 10 + i % 10
            for j in range(n):
                res2 = j // 10 + j % 10
                board[i][j] = res1 + res2

        def helper(i, j):
            # print(board[i][j])
            if board[i][j] > k:
                return 0
            visited.add((i, j))
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n:
                    if (newi, newj) not in visited:
                        helper(newi, newj)

        helper(0, 0)
        return len(visited)


print(Solution().movingCount(16, 8, 4))
