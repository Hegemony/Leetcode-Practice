"""
暴力法
"""


class Solution:
    def isSubstrings(self, s):
        if s == s[::-1]:
            return True
        else:
            return False

    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s) + 1):
            for j in range(i):
                if self.isSubstrings(s[j:i]):
                    # print(j, i, s[j:i])
                    cnt += 1
        return cnt


"""
动态规划法：
利用二维dp: dp[i][j]代表子串[i, j]是否是一个回文串

当i = j时，单个字符肯定是回文串，可以看成奇数回文串的起点
当s[i] = s[j]且 i - j = 1，则dp[j][i]是回文串，可以看成偶数回文串的起点
当s[i] = s[j]且dp[j + 1][i - 1]是回文串，则dp[j][i]也是回文串

"""


class Solution1:
    def countSubstrings(self, s):
        n = len(s)
        dp = [[False for i in range(n)] for i in range(n)]
        count = 0
        # 枚举所有可能， 因为代表子串，所以i <= j
        for i in range(n):
            for j in range(0, i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    count += 1
        print(dp)
        return count


print(Solution1().countSubstrings("abc"))