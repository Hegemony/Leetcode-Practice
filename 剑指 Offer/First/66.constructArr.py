class Solution:
    def constructArr(self, a):
        left = [1 for i in range(len(a))]
        right = [1 for i in range(len(a))]
        res = [1 for i in range(len(a))]
        for i in range(1, len(a)):
            left[i] = left[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            right[i] *= right[i + 1] * a[i + 1]
        print(left, right)
        for i in range(len(a)):
            res[i] = left[i] * right[i]
        return res


print(Solution().constructArr([1, 2, 3, 4, 5]))
