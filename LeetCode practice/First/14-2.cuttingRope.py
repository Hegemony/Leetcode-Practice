class Solution:
    def cuttingRope(self, n: int) -> int:
        res = 0
        for i in range(2, n + 1):
            share = n // i
            extra = n % i
            tmp = share ** (i - extra) * (share + 1) ** extra
            res = max(res, tmp)
        return res % 1000000007