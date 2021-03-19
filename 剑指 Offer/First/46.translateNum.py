class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [1 for i in range(len(num))]
        if len(num) == 1:
            return dp[0]
        if len(num) == 2:
            if int(num) <= 25:
                dp[1] = 2
                return dp[1]
            else:
                return dp[0]
        if num[0:2] <= '25' and num[0] != '0':
            dp[1] = 2
        for i in range(2, len(num)):
            if num[i - 1] == '0':
                dp[i] = dp[i - 1]
            elif num[i - 1:i + 1] <= '25':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]