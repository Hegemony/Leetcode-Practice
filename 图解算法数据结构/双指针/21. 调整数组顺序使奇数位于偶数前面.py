"""
暴力解法
"""
class Solution:
    def exchange(self, nums):
        res1 = []
        res2 = []
        for i in nums:
            if i % 2 == 1:
                res1.append(i)
            if i % 2 == 0:
                res2.append(i)
        return res1 + res2


"""
双指针解法
"""
class Solution1:
    def exchange(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 1:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums
