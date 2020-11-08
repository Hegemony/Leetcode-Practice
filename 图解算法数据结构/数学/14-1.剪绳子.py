"""
看到题目，要使得乘积最大，第一反应就是把n均匀分割

以10分割3份为例。我们首先算出每份的份额share，然后算出多出来的部分extra，然后我们把extra均匀的分配到share里，
也就是有extra份的份额（share）额外多加1，因为余数一定小于除数所以不会有特殊情况。
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        ans = 0
        # 拆分成i份
        for i in range(2, n + 1):
            # 每份的份额为share
            share = n // i
            # 总共多余的部分extra
            extra = n % i
            # 有extra份额外加1，剩下的i-extra份仍然保持原有份额share
            tmp = share ** (i - extra) * (share + 1) ** extra
            ans = max(ans, tmp)
        return ans

"""
动态规划解法：
dp[i] 表示将正整数 i 拆分成至少两个正整数的和之后，这些正整数的最大乘积。

"""
class Solution1:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i-j])
        return dp[n]


print(Solution1().integerBreak(10))