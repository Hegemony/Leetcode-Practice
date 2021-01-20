class Solution:
    def missingNumber(self, nums) -> int:
        """
        O(nlogn)
        """
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i + 1] - nums[i] == 1:
        #         continue
        #     else:
        #         return i + 1
        # return 0 if nums[len(nums) - 1] == len(nums) else len(nums)
        """
        O(n)
        """
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
