class Solution:
    def exist(self, board, word) -> bool:
        def helper(i, j):

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                helper(i, j)
