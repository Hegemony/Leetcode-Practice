"""
迭代法：
"""


class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res


# print(Solution().subsets([1, 2, 3]))

"""
递归：回溯
"""


class Solution1:
    def subsets(self, nums):
        res = []
        l = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            print(res, tmp)
            for j in range(i, l):  # 每个j走一个递归，走完整个列表，进行回溯
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res


print(Solution1().subsets([1, 2, 3]))