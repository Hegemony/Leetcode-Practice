class Solution:
    def permutation(self, s: str):
        res = []
        c = list(s)

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:  # 如果有重复，剪枝
                    continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res


# print(Solution().permutation('abc'))

"""
字符串的全排列代码
"""
class Solution1:
    def permutation(self, s: str):
        if not s:
            return
        s = list(sorted(s))  # sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
        res = []

        def helper(s, tmp):
            if not s:
                res.append(''.join(tmp))
                print('*', res)
            for i, char in enumerate(s):
                if i > 0 and s[i] == s[i - 1]:  # 判重操作，整个字符串，是否有重复的，有重复的字符就跳过，每次的S[i]当作首字母
                    continue
                print(i, tmp, s, char)
                helper(s[:i] + s[i + 1:], tmp + [char])  # 每次取出S[i]当作下一部分字符串的开始

        helper(s, [])
        return res


print(Solution1().permutation('abbc'))

"""
数组的全排列代码
"""
class Solution2:
    def permuteUnique(self, nums):
        res = []
        nums.sort()

        def helper(nums, temp):
            if not nums:
                res.append(temp)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                helper(nums[:i] + nums[i + 1:], temp + [nums[i]])

        helper(nums, [])
        return res
