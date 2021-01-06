class Solution:
    def largeGroupPositions(self, s: str):
        res = []
        n, num = len(s), 1

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    res.append([i - num + 1, i])
                num = 1
            else:
                num += 1

        return res