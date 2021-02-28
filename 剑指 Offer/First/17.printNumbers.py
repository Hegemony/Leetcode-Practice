class Solution:
    def printNumbers(self, n: int):
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res