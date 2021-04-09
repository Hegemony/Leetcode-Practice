class Solution:
    def reverse(self, x: int) -> int:
        res = []
        if x == 0:
            return 0
        elif x > 0:
            while x:
                res.append(x % 10)
                x = x // 10
            tmp = 0
            for i in range(len(res)):
                tmp = tmp * 10 + res[i]
            return tmp if -2 ** 31 <= tmp <= 2 ** 31 else 0
        else:
            x = abs(x)
            while x:
                res.append(x % 10)
                x = x // 10
            tmp = 0
            for i in range(len(res)):
                tmp = tmp * 10 + res[i]
            return -tmp if -2 ** 31 <= tmp <= 2 ** 31 - 1 else 0