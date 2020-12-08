class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res1 = []
        res2 = []
        for i in range(len(s)):
            if i < n:
                res1.append(s[i])
            else:
                res2.append(s[i])
        return ''.join(res2) + ''.join(res1)