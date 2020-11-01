"""
暴力：超时
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0:
            return res
        if n > 0:
            for i in range(n):
                res *= x
            return res
        if n < 0:
            for i in range(abs(n)):
                res /= x
            return res


# print(Solution().myPow(0.00001, 2147483647))

"""
快速幂算法
"""

class Solution1:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            # print(N)
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


print(Solution1().myPow(2, -2))