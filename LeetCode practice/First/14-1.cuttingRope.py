class Solution:
    def cuttingRope(self, n: int) -> int:
        res = 0
        for i in range(2, n + 1):
            share = n // i
            extra = n % i
            summ = (share + 1) ** extra * (share) ** (i - extra)
            res = max(summ, res)
        return res