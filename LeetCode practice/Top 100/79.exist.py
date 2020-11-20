class Solution:
    def exist(self, board, word: str) -> bool:
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n:
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False

