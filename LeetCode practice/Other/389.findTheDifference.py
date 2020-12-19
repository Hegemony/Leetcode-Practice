class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(sorted(s))
        t = list(sorted(t))
        i, j = 0, 0
        l = len(t)
        while i < len(s) and j < len(t) - 1:
            if s[i] != t[j]:
                return t[j]
            i += 1
            j += 1
        return t[l - 1]