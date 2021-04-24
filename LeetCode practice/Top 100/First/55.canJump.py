class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        if n == 0:
            return False
        cur = nums[0]
        for i in range(1, n):
            if i <= cur:
                cur = max(cur, nums[i] + i)
            else:
                return False
        return True