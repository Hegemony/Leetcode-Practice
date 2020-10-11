class Solution:
    def spiralOrder(self, matrix):
        res = []
        row_up, row_down = 0, len(matrix)  # 定义行的上下边界
        col_left, col_right = 0, len(matrix[0])  # 定义列的左右边界
        all = row_down * col_right
        count = 0
        while row_up < row_down and col_left < col_right:
            for i in range(col_left, col_right):    # 从左至右扫描上边界
                res.append(matrix[row_up][i])
                count += 1
            row_up += 1
            if count == all:
                break

            for i in range(row_up, row_down):    # 从上至下扫描右边界
                res.append(matrix[i][col_right - 1])
                count += 1
            col_right -= 1
            if count == all:
                break

            for i in range(col_right - 1, col_left - 1, -1):   # 从右至左扫描下边界
                res.append(matrix[row_down - 1][i])
                count += 1
            row_down -= 1
            if count == all:
                break

            for i in range(row_down - 1, row_up - 1, -1):    # 从下至上扫描下边界
                res.append(matrix[i][col_left])
                count += 1
            col_left += 1
            if count == all:
                break
        return res