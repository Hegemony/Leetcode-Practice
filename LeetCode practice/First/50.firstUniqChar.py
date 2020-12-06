class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for i in s:
            if dic[i] == 1:
                return i
        return ' '