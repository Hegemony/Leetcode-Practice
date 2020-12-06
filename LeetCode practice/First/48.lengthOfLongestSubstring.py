class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 0
        res = 1
        while r < len(s) - 1:
            r += 1
            if s[r] not in s[l:r]:
                res = max(r - l + 1, res)
            else:
                while s[r] in s[l:r]:
                    l += 1
        return res


"""
利用哈希存储每个字符的索引
"""


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        dic = {}
        res = 0
        for i in range(len(s)):
            if s[i] in dic:
                l = max(dic[s[i]], l)
            dic[s[i]] = i

            res = max(res, i - l + 1)
        return res


"aabaab!bb"
"abcabcbb"
"bbbbb"
"pwwkew"

