class Solution:
    def canPartition(self, nums) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        if maxNum > target:
            return False
        """
        dp[i][j] 表示从数组的 [0,i]下标范围内选取若干个正整数（可以是 0 个）
        """
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        # dp[0][nums[0]] = True
        for i in range(1, n + 1):
            num = nums[i - 1]
            print(num)
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        for x in dp:
            print(x)
        return dp[n - 1][target] == 1


print(Solution().canPartition([2, 5, 12, 5]))