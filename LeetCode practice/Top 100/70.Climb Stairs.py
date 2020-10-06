"""
动态规划解法：dp[i]代表爬到第i级台阶的方案数
"""

def climbStairs(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    if n > 1:
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(climbStairs(1))