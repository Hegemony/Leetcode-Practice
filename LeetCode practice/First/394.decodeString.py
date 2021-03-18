class Solution:
    def decodeString(self, s: str) -> str:
        multi = 0
        stack = []
        res = ''
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append([multi, res])
                multi = 0
                res = ''
            elif c == ']':
                cur_multi, cur_res = stack.pop()
                res = cur_res + cur_multi * res
            else:
                res += c
        return res
