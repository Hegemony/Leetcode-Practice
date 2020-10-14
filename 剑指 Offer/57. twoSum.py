"""
暴力解法:超时
"""
class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        res = []
        for i in range(n-1):
            for j in range(i, n):
                if nums[i] + nums[j] == target:
                    res.append(nums[i])
                    res.append(nums[j])
                    break
            if len(res) == 2:
                break
        return res


"""
双指针
"""
class Solution1:
    def twoSum(self, nums, target: int):
        n = len(nums)
        res = []
        left, right = 0, n - 1
        while left < right:
            if nums[left] + nums[right] == target:
                res.append(nums[left])
                res.append(nums[right])
                break
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return res
