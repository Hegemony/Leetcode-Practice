class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0  # 0的位置
        two = len(nums) - 1  # 2的位置
        if len(nums) < 2:
            return

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        i = 0  # 游标
        while i <= two:
            if nums[i] == 0:  # 0的话交换位置，游标i也要+1
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:  # 1的话不用处理
                i += 1
            else:  # 2的话交换位置，游标i不需要改变，因为i过来，two -= 1, 然后在判断交换过来的i再判断是0， 1， 2
                swap(nums, i, two)
                two -= 1
            # print(i, ':', nums)
        # print(zero, two)
        return nums


print(Solution().sortColors([1, 2, 0, 2, 1, 1, 0]))