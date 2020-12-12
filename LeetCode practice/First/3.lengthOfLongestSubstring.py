class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, j = -1, 0
        res = 0
        dic = {}
        while j < len(s):
            print(dic)
            if s[j] in dic:
                l = max(dic[s[j]], l)
            res = max(res, j - l)
            dic[s[j]] = j
            j += 1
        return res
        # if not s:
        #     return 0
        # i, j = 0, 0
        # res = 0
        # while j < len(s):
        #     print(s[i:j])
        #     if s[j] not in s[i:j]:
        #         j += 1
        #     else:
        #         while s[j] in s[i:j]:
        #             i += 1
        #     res = max(res, j - i)
        # return res


print(Solution().lengthOfLongestSubstring('pwwkew'))
