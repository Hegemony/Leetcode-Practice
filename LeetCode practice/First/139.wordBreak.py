class Solution:
    def wordBreak(self, s, wordDict):
        if len(wordDict) == 0:
            return False
        l = len(s)
        dp = [False for i in range(l + 1)]
        dp[0] = True
        for i in range(l):
            for j in range(i + 1, len(s) + 1):
                if (dp[i] and s[i:j] in wordDict):
                    print(s[i:j])
                    dp[j] = True
                    print(i, j)
        print(dp)
        return dp[-1]


print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
