class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                if stack:
                    stack.pop()
                stack += tmp
        return ''.join(stack)