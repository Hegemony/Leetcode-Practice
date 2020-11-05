class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
        return False


print(Solution().findNumberIn2DArray(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))

a = 88
if a >= 90:
    print(u"优秀")
if a == 88:
    print(u"正好88")
if a >= 80:
    print(u"良好")
else:
    print(u"都不合格")

print("* * " * 10)

if a >= 90:
    print(u"优秀")
elif a == 88:
    print(u"正好88")
elif a >= 80:
    print(u"良好")
else:
    print(u"都不合格")
