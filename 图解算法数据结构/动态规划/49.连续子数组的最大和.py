class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        summ = nums[0]
        for i in range(1, len(nums)):
            summ += nums[i]
            dp[i] = max(summ, nums[i])
            if dp[i] == summ:
                continue
            if dp[i] == nums[i]:
                summ = nums[i]
        return max(dp)

"""
 设动态规划列表 dp ，dp[i] 代表以元素 nums[i] 为结尾的连续子数组最大和。
"""
class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)