class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        up, down = 0, m
        left, right = 0, n
        res = []
        cnt, all = 0, m * n
        i, j = 0, 0
        while up < down and left < right:
            for i in range(left, right):
                res.append(matrix[up][i])
                cnt += 1
            up += 1
            if cnt == all:
                return res

            for i in range(up, down):
                res.append(matrix[i][right - 1])
                cnt += 1
            right -= 1
            if cnt == all:
                return res

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[down - 1][i])
                cnt += 1
            down -= 1
            if cnt == all:
                return res

            for i in range(down - 1, up - 1, -1):
                res.append(matrix[i][left])
                cnt += 1
            left += 1
            if cnt == all:
                return res