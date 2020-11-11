"""
超出时间限制
"""


class Solution:
    def constructArr(self, a):
        m = [[1 for i in range(len(a))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a)):
                if j == i:
                    m[i][j] = 1
                else:
                    m[i][j] = a[j]
        b = [1 for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a)):
                b[i] *= m[i][j]

        return b


class Solution1:
    def constructArr(self, a):
        b = [1] * len(a)
        tmp = 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
        return b


"""
l = []这个数组上所有的位置上的数都是原数组此位置上的书的右边的所有元素的乘积，
r = []这个数组上所有的位置上的数都是原数组此位置上的书的左边的所有元素的乘积.
https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/java-pythonchao-xiang-xi-jie-ti-by-yang_hang/
"""


class Solution2:
    def constructArr(self, a):
        l = [1 for i in range(len(a))]
        r = [1 for i in range(len(a))]
        b = [1] * len(a)
        for i in range(1, len(a)):
            l[i] = l[i - 1] * a[i - 1]

        for i in range(len(a) - 2, -1, -1):
            r[i] = r[i + 1] * a[i + 1]
        for i in range(len(b)):
            b[i] = l[i] * r[i]
        return b
