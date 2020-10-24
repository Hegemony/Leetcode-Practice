class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        n = len(str)
        if n == 0:
            return 0
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if str[0] != '-' and str[0] != '+' and str[0] not in a:
            return 0
        res = []
        sums = 0
        if str[0] == '-':
            for i in range(1, n):
                if str[i] in a:
                    res.append(str[i])
                else:
                    break
            l = len(res)
            sums = 0
            e = 0
            for i in range(l - 1, -1, -1):
                sums += int(res[i]) * (10 ** e)
                e += 1
            if sums >= 2 ** 31:
                sums = -2 ** 31
            else:
                sums = -sums

        if str[0] == '+':
            for i in range(1, n):
                if str[i] in a:
                    res.append(str[i])
                else:
                    break
            l = len(res)
            sums = 0
            e = 0
            for i in range(l - 1, -1, -1):
                sums += int(res[i]) * (10 ** e)
                e += 1
            if sums >= 2 ** 31:
                sums = 2 ** 31 - 1
            else:
                sums = sums

        if str[0] != '-' and str[0] != '+':
            if str[0] in a:
                res.append(str[0])
                for i in range(1, n):
                    if str[i] in a:
                        res.append(str[i])
                    else:
                        break
                l = len(res)
                sums = 0
                e = 0
                for i in range(l - 1, -1, -1):
                    sums += int(res[i]) * (10 ** e)
                    e += 1
                if sums >= 2 ** 31:
                    sums = 2 ** 31 - 1
                else:
                    sums = sums
        return sums


print(Solution().strToInt('+1'))


"""
题解：
字符转数字： “此数字的 ASCII 码” 与 “ 0 的 ASCII 码” 相减即可；
数字拼接： 若从左向右遍历数字，设当前位字符为 c ，当前位数字为 x，数字结果为 res，则数字拼接公式为：
res = 10 * res + x
x = ascii(c)−ascii('0')

ord():可以将字符转化为你所需要的ASCII码
"""
class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()  # 删除首尾空格
        if not str:
            return 0  # 字符串为空则直接返回
        res, i, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if str[0] == '-':
            sign = -1  # 保存负号
        elif str[0] != '+':
            i = 0  # 若无符号位，则需从 i = 0 开始数字拼接
        for c in str[i:]:
            if not '0' <= c <= '9':
                break  # 遇到非数字的字符则跳出
            if res > bndry or res == bndry and c > '7':
                return int_max if sign == 1 else int_min  # 数字越界处理
            res = 10 * res + ord(c) - ord('0')  # 数字拼接
        return sign * res

