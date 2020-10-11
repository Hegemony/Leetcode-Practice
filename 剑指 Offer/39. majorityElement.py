class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        n = len(nums)
        if n == 1:
            return nums[0]
        return nums[n // 2]

