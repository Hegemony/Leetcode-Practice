class Solution:
    def minArray(self, numbers) -> int:
        numbers.sort()
        return numbers[0]