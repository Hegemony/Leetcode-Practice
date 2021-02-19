class Solution:
    def findRepeatNumber(self, nums) -> int:
        res = set()
        for i in range(len(nums)):
            if nums[i] not in res:
                res.add(nums[i])
            else:
                return nums[i]