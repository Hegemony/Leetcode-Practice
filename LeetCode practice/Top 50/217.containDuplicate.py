class Solution:
    def containsDuplicate(self, nums) -> bool:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            if dic[nums[i]] >= 2:
                return True
        return False