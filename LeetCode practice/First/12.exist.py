class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        visited = set()

        def helper(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n:
                    if (newi, newj) not in visited:
                        if helper(newi, newj, k + 1):
                            print(visited)
                            return True

            visited.remove((i, j))

        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True
        return False


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
