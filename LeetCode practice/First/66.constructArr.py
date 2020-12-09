class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        left = [1 for i in range(len(a))]
        right = [1 for i in range(len(a))]
        res = [1 for i in range(len(a))]
        for i in range(1, len(a)):
            left[i] = left[i - 1] * a[i - 1]
        for j in range(len(a) - 2, -1, -1):
            right[j] = right[j + 1] * a[j + 1]
        for i in range(len(a)):
            res[i] = left[i] * right[i]
        return res