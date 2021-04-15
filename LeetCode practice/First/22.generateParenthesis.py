class Solution:
    def generateParenthesis(self, n: int):
        res = []
        tmp = []

        def dfs(left, right):
            if left == n and right == n:
                res.append(''.join(tmp))
                return
            if left < right:
                return
            if left < n:
                tmp.append('(')
                dfs(left + 1, right)
                tmp.pop()
            if right < n:
                tmp.append(')')
                dfs(left, right + 1)
                tmp.pop()
        dfs(0, 0)
        return res


print(Solution().generateParenthesis(3))
