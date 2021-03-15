#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self , s ):
        # write code here
        if len(s) % 2 == 1:
            return False
        if len(s) == 0:
            return True
        dic = {')': '(', ']': '[', '}': '{'}
        res = []
        for i in s:
            if i in dic.values():
                res.append(i)
            else:
                if len(res) == 0:
                    return False
                if res.pop() != dic[i]:
                    return False
        return len(res) == 0
