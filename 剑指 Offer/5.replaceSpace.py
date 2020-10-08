"""
str.replace(old, new[, max])
参数
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        ss = s.replace(' ', '%20')
        return ss

print(Solution().replaceSpace("We are happy."))