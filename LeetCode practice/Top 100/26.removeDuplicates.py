class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        j = 0
        if len(nums) == 0:
            return 0

        for _ in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
            # print(nums)
        return i + 1
