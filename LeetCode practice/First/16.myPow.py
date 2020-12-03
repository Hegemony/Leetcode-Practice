"""
暴力超时
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if x > 0:
            for i in range(n):
                res *= x
            return res
        elif x == 0:
            return 0
        else:
            x = -x
            for i in range(n):
                res *= x
            res = 1 / res
            return res


"""
矩阵快速幂
"""


class Solution1:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            if N % 2 == 0:
                return y * y
            else:
                return y * y * x

        if n >= 0:
            return quickMul(n)
        else:
            return 1.0 / quickMul(-n)  # -n -> -(-2)
