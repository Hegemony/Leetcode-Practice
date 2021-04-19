class Solution:
    def exist(self, board, word: str) -> bool:
        n, m = len(board), len(board[0])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = []

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.append((i, j))
            for di, dj in direction:
                newi, newj = i + di, j + dj
                if 0 <= newi < n and 0 <= newj < m and (newi, newj) not in visited:
                    if dfs(newi, newj, k + 1):
                        return True
            visited.pop()
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
