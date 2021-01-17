class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = '0'
        if len(s) == 0:
            return 0
        if s[0] == '-':
            for i in range(1, len(s)):
                if '0'<= s[i] <='9':
                    res += s[i]
                else:
                    break
            return -2 ** 31 if int(res) > 2 ** 31 else -int(res)
        elif s[0] == '+':
            for i in range(1, len(s)):
                if '0'<= s[i] <='9':
                    res += s[i]
                else:
                    break
            return 2 ** 31 - 1 if int(res) > 2 ** 31 - 1 else int(res)
        elif '0'<= s[0] <='9':
            for i in range(len(s)):
                if '0'<= s[i] <='9':
                    res += s[i]
                else:
                    break
            return 2 ** 31 - 1 if int(res) > 2 ** 31 - 1 else int(res)
        else:
            return 0