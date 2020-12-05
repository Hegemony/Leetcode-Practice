"""
超时
"""


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        res = []
        nums.sort()

        def helper(nums, tmp):
            if len(nums) == 0:
                res.append(''.join(tmp))
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                helper(nums[:i] + nums[i + 1:], tmp + str(nums[i]))

        helper(nums, '')
        return min(res)


"""
3 + 30 = 330
30 + 3 = 303
330 > 303
则30 < 3
"""


class Solution1:
    def minNumber(self, nums) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        """
        冒泡排序
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)


class Solution2:
    def quciksort(self, nums):
        