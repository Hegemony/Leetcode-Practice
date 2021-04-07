class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            dic[num] = index
        for i, num in enumerate(nums):
            j = dic.get(target - num)
            if j is not None and i != j:
                return [i, j]