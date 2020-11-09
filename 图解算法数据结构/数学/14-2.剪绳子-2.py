class Solution:
    def cuttingRope(self, n: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            share = n // i
            extra = n % i

            tmp = (share + 1) ** extra * share ** (i - extra)

            ans = max(tmp, ans)

        return ans % 1000000007


print(Solution().cuttingRope(2))


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n] % 1000000007

