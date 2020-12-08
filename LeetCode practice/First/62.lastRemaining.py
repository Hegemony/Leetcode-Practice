class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        a = list(range(n))
        i = 0
        while len(a) > 1:
            i = (i + m - 1) % len(a)
            a.pop(i)
        return a[0]


print(Solution().lastRemaining(5, 3))
