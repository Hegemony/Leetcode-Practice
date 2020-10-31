class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        if len(s) == 1:
            return 1
        dp = [1 for i in range(len(s) + 1)]
        for i in range(2, len(s) + 1):
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '5'):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
