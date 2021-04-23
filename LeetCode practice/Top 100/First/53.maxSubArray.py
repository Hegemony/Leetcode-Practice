class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        print('dp', dp)
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        print(dp)
        return max(dp)


print(Solution().maxSubArray([1]))
