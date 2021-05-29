class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res