"""
暴力解法
"""
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        if n == 0:
            return []
        result = []
        for i in range(n - k + 1):
            res = []
            for j in range(i, i + k):
                res.append(nums[j])
            result.append(max(res))
        return result
