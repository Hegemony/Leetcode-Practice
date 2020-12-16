class Solution:
    def sortColers(self, nums):
        """
        两次遍历
        :param nums:
        :return:
        """
        # n = len(nums)
        # flag = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         nums[i], nums[flag] = nums[flag], nums[i]
        #         flag += 1
        # for i in range(flag, n):
        #     if nums[i] == 1:
        #         nums[i], nums[flag] = nums[flag], nums[i]
        #         flag += 1
        """
        一次遍历：
        双指针
        """
        zero, two = 0, len(nums) - 1
        if len(nums) < 2:
            return

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        i = 0
        while i <= two:
            if nums[i] == 0:
                swap(nums, i, zero)
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, two)
                two -= 1