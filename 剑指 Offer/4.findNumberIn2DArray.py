class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix:  # 二维数组为空
            return False
        n = len(matrix)     # 行
        m = len(matrix[0])  # 列
        for i in range(n):
            for j in range(m):
                if target == matrix[i][j]:
                    return True
        return False


# a = [[0]*3] *4
# print(a)
# print(len(a), len(a[0]))
# print(a[0])
# b = [0 for i in range(6)]
# print(b)
