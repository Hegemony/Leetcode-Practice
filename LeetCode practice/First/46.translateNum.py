class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        if len(s) == 1:
            return 1
        dp = [1 for i in range(len(s))]
        if int(s[0] + s[1]) <= 25 and s[0] != '0' :
            dp[1] = 2
        for i in range(2, len(s)):
            if int(s[i - 1] + s[i]) > 25:
                dp[i] = dp[i - 1]
            elif s[i - 1] == '0':
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]