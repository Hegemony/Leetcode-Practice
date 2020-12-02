import math

"""
暴力解：超时
numSquares(n) = min(numSquares(n-k) + 1)
"""


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        def MinNumSquares(k):
            if k in square_nums:
                return 1
            min_num = float('inf')

            for square in square_nums:
                if k < square:
                    break
                new_num = MinNumSquares(k - square) + 1
                min_num = min(new_num, min_num)
            return min_num

        return MinNumSquares(n)


class Solution1:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, int(i ** (0.5)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                print(i, dp[i], dp)
        return dp[-1]


print(Solution1().numSquares(25))
