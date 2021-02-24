class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]