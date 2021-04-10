class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        传统做法
        :param s:
        :return:
        """
        # i, j = 0, 0
        # res = 0
        # while j < len(s):
        #     if s[j] not in s[i:j]:
        #         j += 1
        #     else:
        #         while s[j] in s[i:j]:
        #             i += 1
        #     res = max(res, j - i)
        # return res
        """
        字典做法
        """
        l = -1
        dic = {}
        i = 0
        res = 0
        while i < len(s):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                l = max(l, dic[s[i]])
                dic[s[i]] = i
            res = max(res, i - l)
            i += 1
        return res


print(Solution().lengthOfLongestSubstring('tmmzuxt'))