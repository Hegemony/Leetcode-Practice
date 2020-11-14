"""
暴力解法：时间复杂度高
"""


class Solution:
    def generateParenthesis(self, n: int):
        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
                print(A)

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans


"""
暴力法的改进：回溯法
如果左括号数量不大于 nn，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。
"""


class Solution1:
    def generateParenthesis(self, n: int):
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
                # print('left:', left)
                # print('1:', S)
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()
                # print('right:', right)
                # print('2:', S)

        backtrack([], 0, 0)
        return ans


print(Solution1().generateParenthesis(3))
