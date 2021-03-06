class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        row_up, row_down = 0, m
        col_left, col_right = 0, n
        cnt, all = 0, m * n
        while row_up < row_down and col_left < col_right:
            for i in range(col_left, col_right):
                res.append(matrix[row_up][i])
                cnt += 1
            row_up += 1
            if cnt == all:
                break
            for i in range(row_up, row_down):
                res.append(matrix[i][col_right - 1])
                cnt += 1
            col_right -= 1
            if cnt == all:
                break

            for i in range(col_right - 1, col_left - 1, -1):
                res.append(matrix[row_down - 1][i])
                cnt += 1
            row_down -= 1
            if cnt == all:
                break

            for i in range(row_down - 1, row_up - 1, -1):
                res.append(matrix[i][col_left])
                cnt += 1
            col_left += 1
            if cnt == all:
                break
        return res