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
