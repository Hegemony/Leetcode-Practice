class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        l = int(n / 2)
        nums.sort()
        if nums[l] == nums[l - 1] or nums[l] == nums[l + 1]:
            return nums[l]


a = Solution()
Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
