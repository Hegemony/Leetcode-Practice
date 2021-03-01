class Solution:
    def exchange(self, nums):
        # res1, res2 = [], []
        # for num in nums:
        #     if num % 2 == 0:
        #         res2.append(num)
        #     else:
        #         res1.append(num)
        # return res1 + res2
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return nums