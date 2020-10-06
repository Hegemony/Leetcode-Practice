"""
错误做法：
输入：
[2,1,1,2]
输出：
3
预期结果：
4
"""
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        cur_money1 = 0
        cur_money2 = 0
        for i in range(0, n, 2):
            cur_money1 += nums[i]
        for j in range(1, n, 2):
            cur_money2 += nums[j]
        return max(cur_money1, cur_money2)


"""
如果房屋数量大于两间，应该如何计算能够偷窃到的最高总金额呢？对于第 k (k>2) 间房屋，有两个选项：

偷窃第 k 间房屋，那么就不能偷窃第 k-1 间房屋，偷窃总金额为前 k-2 间房屋的最高总金额与第 k 间房屋的金额之和。

不偷窃第 k 间房屋，偷窃总金额为前 k-1 间房屋的最高总金额。

在两个选项中选择偷窃总金额较大的选项，该选项对应的偷窃总金额即为前 k 间房屋能偷窃到的最高总金额。

用 dp[i] 表示前 i 间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：

dp[i]=max(dp[i−2]+nums[i],dp[i−1])

边界条件为：
dp[0]=nums[0]   只有一间房屋，则偷窃该房屋
dp[1]=max(nums[0],nums[1])   只有两间房屋，选择其中金额较高的房屋进行偷窃

最终的答案即为 dp[n−1]，其中 nn 是数组的长度。
"""

class Solution1:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]