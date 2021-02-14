class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 0:
            return
        res = []
        nums = set(nums)
        for i in range(1, l + 1):
            if i not in nums:
                res.append(i)
        return res