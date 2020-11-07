class Solution:
    def twoSum(self, nums, target: int):
        l, r = 0, len(nums) - 1
        res = []
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                res.append(nums[l])
                res.append(nums[r])
                break
        return res