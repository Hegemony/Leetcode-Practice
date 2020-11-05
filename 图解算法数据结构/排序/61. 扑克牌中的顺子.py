class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        n = nums.count(0)
        s = set()
        for i in range(n):
            nums.pop(0)
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return False
        if nums[-1] - nums[0] <= 4:
            return True
        else:
            return False