class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        for i in range(len(nums)):
            if dic[nums[i]] == 1:
                return nums[i]