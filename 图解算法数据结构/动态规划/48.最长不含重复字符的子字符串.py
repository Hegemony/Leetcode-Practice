"""
超出时间限制
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        dp = [0 for i in range(len(s))]
        dp[0] = 1
        i = 0
        for j in range(len(s)):
            if s[j] not in s[i:j]:
                dp[j] = j - i + 1
            else:
                for m in range(j):
                    if s[m] == s[j]:
                        i = m + 1
        return max(dp)

print(Solution().lengthOfLongestSubstring("abba"))

"""
滑动窗口方法：
"""
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        win = []
        res = 0
        result = 0
        for i in range(len(s)):
            res += 1
            while s[i] in win:
                win.pop(0)
                res -= 1
            win.append(s[i])
            result = max(res, result)
        return result

print(Solution1().lengthOfLongestSubstring("abba"))


"""
动态规划做法：
状态定义： 设动态规划列表 dp ，dp[j] 代表以字符 s[j]为结尾的 “最长不重复子字符串” 的长度。
转移方程： 固定右边界 j，设字符 s[j] 左边距离最近的相同字符为 s[i] ，即 s[i] = s[j]。

当 i < 0 ，即 s[j] 左边无相同字符，则 dp[j] = dp[j-1] + 1；
当 dp[j - 1] < j - i ，说明字符 s[i] 在子字符串 dp[j-1] 区间之外 ，则 dp[j] = dp[j - 1] + 1；
当 dp[j - 1] > j - i ，说明字符 s[i]在子字符串 dp[j-1]区间之中 ，则 dp[j] 的左边界由 s[i] 决定，即 dp[j] = j - i；
当 i < 0 时，由于 dp[j - 1] ≤j 恒成立，因而 dp[j - 1] < j - i恒成立，因此分支 1. 和 2. 可被合并。

dp[j]={ dp[j−1]+1 ,  dp[j−1]<j−i
        j−i   ,      dp[j−1]≥j−i
返回值： max(dp) ，即全局的 “最长不重复子字符串” 的长度。

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)   # 获取索引 i
            dic[s[j]] = j    # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i   # dp[j - 1] -> dp[j]
            res = max(res, tmp)   # max(dp[j - 1], dp[j])
        return res