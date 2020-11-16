class Solution:
    def permute(self, nums):
        nums = sorted(nums)
        res = []
        def helper(nums, temp):
            if not nums:
                res.append(temp)
            for i in range(len(nums)):
                print(temp)
                helper(nums[:i] + nums[i+1:], temp + [nums[i]])
            return


        helper(nums, [])
        return res

print(Solution().permute([1, 2, 3]))
