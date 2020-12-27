class Solution:
    def canJump(self, nums):
        if len(nums) == 0:
            return False
        l = len(nums)
        cur = nums[0]
        for i in range(1, l):
            if i <= cur:
                cur = max(cur, nums[i] + l)
            else:
                return False
        return True
