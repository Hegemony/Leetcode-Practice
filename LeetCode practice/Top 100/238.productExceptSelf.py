"""
构建left,right数组
"""
class Solution:
    def productExceptSelf(self, nums):
        l = len(nums)
        left = [1 for i in range(l)]
        right = [1 for i in range(l)]
        res = [1 for i in range(l)]
        for i in range(1, l):
            left[i] = left[i - 1] * nums[i - 1]
        for j in range(l - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]
        for i in range(l):
            res[i] = left[i] * right[i]
        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
