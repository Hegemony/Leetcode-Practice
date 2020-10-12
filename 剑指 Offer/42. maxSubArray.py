"""
转移方程： 若 dp[i-1] ≤0 ，说明 dp[i - 1]对 dp[i]产生负贡献，即 dp[i-1] + nums[i]不如 nums[i]本身大。

当 dp[i - 1] > 0时：执行 dp[i] = dp[i-1] + nums[i] ；
当 dp[i - 1] ≤0 时：执行 dp[i] = nums[i]；
"""
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        print(dp)
        return max(dp)