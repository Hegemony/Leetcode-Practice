class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i - 1]:
                return numbers[i]
        return numbers[0]