"""
可以用join函数的情况
"""
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        l, r = 0, 0
        res1 = []
        res2 = []
        for i in range(len(s)):
            if r < n:
                res1.append(s[i])
                r += 1
            else:
                res2.append(s[i])
        return ''.join(res2 + res1)


"""
如果不允许用join函数
"""
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res
