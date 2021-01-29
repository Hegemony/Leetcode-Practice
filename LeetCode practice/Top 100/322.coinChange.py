class Solution:
    def coinChange(self, coins, amount: int) -> int:
        f = [float('inf') for i in range(amount + 1)]
        f[0] = 0
        for c in coins:  # 对每个零钱，一种零钱为一行
            for j in range(c, amount + 1):   # 每列代表当前体积j下花费零钱的最小数量
                f[j] = min(f[j], f[j - c] + 1)
        return f[amount] if f[amount] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。