"""
标准递归：写法超时
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return (self.fib(n-1) + self.fib(n-2)) % 1000000007

print(Solution().fib(3))

"""
动态规划：dp[i]为dp[i-1]和dp[i-2]的和
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0 for i in range(n+1)]  # 长度为n的列表
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n] % 1000000007
