class Solution:
    def decodeString(self, s: str) -> str:
        """
        利用辅助栈的做法：随时保存更新res
        """
        stack, res, multi = [], "", 0
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append([multi, res])
                res, multi = '', 0
            elif c == ']':
                cur_multi, last_res = stack.pop()  # 从后向前弹出
                res = last_res + cur_multi * res
            else:
                res += c
        return res