"""
回溯法
"""


class Solution:
    def subsets(self, nums):
        res = []

        def helper(index, tmp):
            res.append(tmp)
            print(res)
            for i in range(index, len(nums)):
                helper(i + 1, tmp + [nums[i]])

        helper(0, [])
        return res


# print(Solution().subsets([1, 2, 3]))

"""
迭代法
"""


class Solution1:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            for j in res:
                res = res + [j + [i]]
            print(res)
        return res


print(Solution1().subsets([1, 2, 3]))

a = [1, 2, 3]
"""
python中 + 和 append的区别
"""
for i in a:
    a = a + [4]
    print(len(a))
    print(a)

# b = [1, 2, 3]
# for i in b:
#     b.append(4)
#     print(b)
