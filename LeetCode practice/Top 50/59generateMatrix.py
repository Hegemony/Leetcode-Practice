class Solution:
    def generateMatrix(self, n: int):
        all = n * n + 1
        cnt = 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        up, down, left, right = 0, n, 0, n
        while up < down and left < right:
            for i in range(left, right):
                res[up][i] = cnt
                cnt += 1
            up += 1
            if cnt == all:
                return res

            for i in range(up, down):
                res[i][right - 1] = cnt
                cnt += 1
            right -= 1
            if cnt == all:
                return res

            for i in range(right - 1, left - 1, -1):
                res[down - 1][i] = cnt
                cnt += 1
            down -= 1
            if cnt == all:
                return res

            for i in range(down - 1, up - 1, -1):
                res[i][left] = cnt
                cnt += 1
            left += 1
            if cnt == all:
                return res
