"""
自己的错解
"""


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if len(wordDict) == 0:
            return False
        l = len(s)
        i = 0
        left = 0
        while i < l:
            ss = s[left:i + 1]
            print(ss)
            if ss in wordDict:
                left = i + 1
                i += 1
            else:
                i += 1
        if left == l:
            return True
        else:
            return False


# print(Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]))

"""
动态规划解法:
初始化 dp=[False,⋯,False]，长度为 n+1。n 为字符串长度。dp[i] 表示 s 的前 i 位是否可以用 wordDict 中的单词表示。

首先，s[0:4]=='leet' 是wordDict内的单词，所以dp[4]=True。
继续以0为起点，4以后的索引为终点的单词都不在字典内，选择忽略。
即'leetc','leetco','leetcod','leetcode'都不在字典内，忽略不管。

第二步，因为之前设置了DP[4]=True,所以迭代至4为起点
查看后面的单词是否在字典内。发现s[4:8]=='code' 在字典内，
所以设置DP[8]为True，至此循环结束。
返回DP[-1] 若是True，则表示能够拆分
"""


class Solution1:
    def wordBreak(self, s: str, wordDict) -> bool:
        if len(wordDict) == 0:
            return False
        l = len(s)
        dp = [False for i in range(l + 1)]
        dp[0] = True
        for i in range(len(s)):
            for j in range(i + 1, len((s)) + 1):
                print('-', i, j)
                if (dp[i] and (s[i:j] in wordDict)):
                    print(s[i:j])
                    print(i, j)
                    dp[j] = True
        print(dp)
        return dp[-1]


print(Solution1().wordBreak("aaaaaaa", ["aaaa", "aaa"]))
