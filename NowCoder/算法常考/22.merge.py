#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return void
#
class Solution:
    def merge(self, A, m, B, n):
        # write code here
        while m > 0 and n > 0:
            if A[m - 1] >= B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1
        if n > 0:
            A[:n] = B[:n]
        return A


print(Solution().merge([], 0, [1], 1))
