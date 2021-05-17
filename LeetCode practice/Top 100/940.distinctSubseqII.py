class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dic = {}
        dp = [1]
        for i in range(len(s)):
            dp.append(dp[-1] * 2)
            if s[i] in dic:
                dp[-1] -= dp[dic[s[i]]]
            dic[s[i]] = i
            print(dp)
        return (dp[-1] - 1) % (1000000000 + 7)
