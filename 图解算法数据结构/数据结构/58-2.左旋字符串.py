class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        l = len(s)
        res = []
        for i in range(n, l):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)