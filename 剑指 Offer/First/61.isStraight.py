class Solution:
    def isStraight(self, nums ) -> bool:
        nums.sort()
        n = len(nums)
        cnt = nums.count(0)
        i = cnt
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                return False
            i += 1
        if nums[n - 1] - nums[cnt] <= 4:
            return True
        return False