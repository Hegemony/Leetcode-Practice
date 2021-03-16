#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self, str1, str2):
        # write code here
        dp = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
        maxx = 0
        di, dj = 0, 0
        for i in range(len(str1) + 1):
            for j in range(len(str2) + 1):
                if dp[i][j] > maxx:
                    maxx = dp[i][j]
                    di = i
                    dj = j
        return str1[di - maxx:di]


print(Solution().LCS("1AB2345CD", "12345EF"))
