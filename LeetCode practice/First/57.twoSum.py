class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        res = []
        while i < j:
            if nums[i] + nums[j] == target:
                res.append(nums[i])
                res.append(nums[j])
                break
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return res