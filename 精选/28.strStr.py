class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return 0
        l = len(needle)
        i, j = 0, l - 1
        while j < len(haystack):
            if needle == haystack[i:j + 1]:
                return i
            else:
                i += 1
                j += 1
        return -1