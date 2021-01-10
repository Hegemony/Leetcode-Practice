class Solution:
    def plusOne(self, digits):
        res = []
        tmp = 0
        for i in range(len(digits)):
            tmp = tmp * 10 + digits[i]
        if tmp == 0:
            for i in range(len(digits) - 1):
                res.append(0)
            res.append(1)
        else:
            tmp += 1
            while tmp:
                res.append(tmp % 10)
                tmp = tmp // 10
            res.reverse()
            return res