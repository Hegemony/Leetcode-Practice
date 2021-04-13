class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res