class Solution:
    def findTargetSumWays(self, nums, S) -> int:
        maxSum = sum(nums)
        target = maxSum - S
        # 如果总和小于S，或者两者差值不被2整除，那么不可能存在满足条件的组合，提前终止
        if target < 0 or target % 2 != 0:
            return 0
        target //= 2
        """
        给定一个数组和一个容量为x的背包，求有多少种方式让背包装满。
        dp[i][j]： i(1 ~ len)表示遍历（不一定选）了 i 个元素，j(0 ~ sum) 表示它们的和
        1.初始化：0个元素，和为0，情况有1种（因为没有元素，所以只能不选，和为0）：dp[0][0] = 1    
        2.不选当前元素，即"部分和"(即j)与之前相同：dp[i][j] = dp[i - 1][j]
        3.可选可不选，不选的情况是2，选当前元素的话则之前的状态应为dp[i - 1][j - num]（这里的num指的是当前元素的值，即代码中的nums[i - 1]），二者相加，即：dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num]
        """
        dp = [[0 for i in range(target + 1)] for j in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(0, target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[-1][-1]
