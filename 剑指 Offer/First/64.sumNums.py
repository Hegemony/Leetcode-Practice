class Solution:
    def sumNums(self, n: int) -> int:
        self.res = 0

        def helper(n):
            if n > 0:
                self.res += n
                helper(n - 1)
            else:
                return
        helper(n)
        return self.res