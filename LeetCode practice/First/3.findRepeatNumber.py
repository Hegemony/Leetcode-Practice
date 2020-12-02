class Solution:
    def findRepeatNumber(self, nums) -> int:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        for i in dic:
            if dic[i] >= 2:
                return i


print(Solution().findRepeatNumber([2, 3, 3, 2, 3, 1]))