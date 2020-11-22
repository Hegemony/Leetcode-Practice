"""
G(n): 长度为 n的序列能构成的不同二叉搜索树的个数。

F(i, n): 以 i为根、序列长度为 n的不同二叉搜索树个数 (1≤i≤n)。

G(n)= i=1∑n F(i,n)
F(i,n)=G(i−1)⋅G(n−i)

G(n)= i=1∑n G(i−1)⋅ G(n−i)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


"""
利用卡特兰数公式计算
"""
class Solution1(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) / (i + 2)
        return int(C)
