import functools


class Solution:
    def minNumber(self, nums) -> str:
        """
        冒泡排序
        :param nums:
        :return:
        """
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
        #             nums[j], nums[i] = nums[i], nums[j]
        #         else:
        #             pass
        # nums = list(map(str, nums))
        """
        自定义排序
        """

        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(nums)
