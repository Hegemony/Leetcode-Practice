class Solution:
    def majorityElement(self, nums) -> int:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        for i in dic:
            if dic[i] > (len(nums) // 2):
                return i