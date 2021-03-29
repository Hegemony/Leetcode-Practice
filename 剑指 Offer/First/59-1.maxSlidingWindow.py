class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        if len(nums) == 0:
            return 0
        i, j = 0, k - 1
        while j < len(nums):
            res.append(max(nums[i:j + 1]))
            j += 1
            i += 1
        return res