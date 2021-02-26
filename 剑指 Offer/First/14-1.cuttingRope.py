class Solution:
    def cuttingRope(self, n: int) -> int:
        res = 0
        for i in range(2, n + 1):
            cnt = n // i
            yu = n % i
            res = max(res, (cnt + 1) ** yu * cnt ** (i - yu))
        return res