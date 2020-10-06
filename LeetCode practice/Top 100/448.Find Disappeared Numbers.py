"""
暴力：
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        # nums.sort()
        n = len(nums)
        if n == 0:
            return
        a = set()
        res = []
        for i in nums:
            if i not in a:
                a.add(i)

        for j in range(1, n + 1):
            print(j)
            if j not in a:
                res.append(j)

        return res


print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
# print(Solution().findDisappearedNumbers([1, 1]))

