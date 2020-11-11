class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, n - 1
        u, d = 0, m - 1
        res = []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[u][i])    # 从左到右
            u += 1
            if u > d:
                break
            for i in range(u, d + 1):
                res.append(matrix[i][r])    # 从上到下
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):   # 从右到左
                res.append(matrix[d][i])
            d -= 1
            if u > d:
                break
            for i in range(d, u - 1, -1):   # 从下到上
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res