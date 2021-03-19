class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        初始做法
        :param s:
        :return:
        """
        # if len(s) < 2:
        #     return len(s)
        # i, j = 0, 0
        # res = 1
        # while j < len(s) - 1:
        #     j += 1
        #     if s[j] not in s[i:j]:
        #         j += 1
        #         res = max(j - i + 1, res)
        #     else:
        #         while s[j] in s[i:j]:
        #             i += 1
        #     return res
        """
        字典的方法
        """
        if len(s) < 2:
            return len(s)
        dic = {}
        l = -1
        res = 0
        for i in range(len(s)):
            if s[i] in dic:
                l = max(dic[s[i]], l)
            dic[s[i]] = i
            res = max(res, i - l)
        return l


print(Solution().lengthOfLongestSubstring('aaaaabbbc'))
