"""
下面思路可能更容易理解。
所以状态表示就是这样的：dp[i][j]，表示投掷完 i 枚骰子后，点数 j 的出现次数。
单单看第 n枚骰子，它的点数可能为 1 , 2, 3, ... , 6因此投掷完 n枚骰子后点数 j出现的次数，可以由投掷完 n-1枚骰子后，对应点数 j-1, j-2, j-3, ... , j-6出现的次数之和转化过来。


n个骰子，一共有6**n种情况
n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
可以看作是从前(n-1)个骰子投完之后的状态转移过来。
其中F（N,S）表示投第N个骰子时，点数和为S的次数
"""
class Solution:
    def twoSum(self, n: int):
        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, n+1):
            for j in range(i, i*6+1):
                for k in range(1, 7):
                    if j > k:
                        dp[i][j] += dp[i-1][j-k]
        res = []
        for i in range(n, n*6+1):
            res.append(dp[n][i]*1.0 / 6**n)
        print(dp)
        return res

print(Solution().twoSum(3))