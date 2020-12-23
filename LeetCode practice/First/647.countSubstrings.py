"""
动态规划法：
利用二维dp: dp[j][i]代表子串[j, i]是否是一个回文串

当i = j时，单个字符肯定是回文串，可以看成奇数回文串的起点
当s[i] = s[j]且 i - j = 1，则dp[j][i]是回文串，可以看成偶数回文串的起点
当s[i] = s[j]且dp[j + 1][i - 1]是回文串，则dp[j][i]也是回文串

"""


class Solution:
    def countSubstrings(self, s):
        n = len(s)
        dp = [[False for i in range(n)] for i in range(n)]
        count = 0
        # 枚举所有可能， 因为代表子串，所以j <= i
        for i in range(n):
            for j in range(0, i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    """
                    比如dp[0][4]需要知道dp[1][3]，而dp[1][3]又是通过dp[2][2]计算出来的，dp[0][4]是i=4时才能计算的，
                    dp[1][3]是i=3时已经计算的，而dp[2][2]是i=2时就计算的，所以对于dp[j+1][i-1]的状态的计算永远先于dp[j][i]的计算，
                    无需担心计算dp[j][i]时还不知道dp[j+1][i-1]的状态。
                    """
                    dp[j][i] = 1
                    count += 1
            print(dp)
        return count


print(Solution().countSubstrings("aba"))

"""
中心扩散法：
"""


class Solution1:
    def countSubstrings(self, s):
        # aaababa #单数中心，双数中心 #aaaa
        # ababa #a,bab,ababa
        def speard(l, r):
            count = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        ans = 0
        for i in range(len(s)):
            ans += speard(i, i)
        for i in range(len(s) - 1):
            ans += speard(i, i + 1)
        return ans
