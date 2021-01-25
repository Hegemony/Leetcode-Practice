class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        y = x.copy()
        y.reverse()
        return x == y