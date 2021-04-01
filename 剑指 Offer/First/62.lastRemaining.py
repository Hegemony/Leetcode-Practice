class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        res = [i for i in range(n)]
        flag = 0
        while len(res) > 1:
            flag = (flag + m - 1) % len(res)
            res.pop(flag)
        return res[-1]


class Solution1:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x
