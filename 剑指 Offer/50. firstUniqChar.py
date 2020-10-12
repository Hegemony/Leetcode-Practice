"""
有错
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ' '
        res = []
        for i in range(n):
            if s[i] not in res:
                res.append(s[i])
            else:
                res.remove(s[i])
        if len(res) == 0:
            return ' '
        return res[0]


print(Solution().firstUniqChar("leetcode"))
# print(Solution().firstUniqChar("loveleetcode"))


"""
题解：哈希表，有序哈希表

dict.get(key, default=None)
# key -- 字典中要查找的键。
# default -- 如果指定键的值不存在时，返回该默认值。
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in s:
            if dic[c] == 1:
                return c
        return ' '
