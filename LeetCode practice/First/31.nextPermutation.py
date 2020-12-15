class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # 从后到前找到nums[i] < nums[i + 1]的数
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:  # 在从后找到nums[j] > nums[i]的数，进行调换
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:   # 将交换的位置之后的所有元素进行交换
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1