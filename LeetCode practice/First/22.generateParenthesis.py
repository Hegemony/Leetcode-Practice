class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(curStr, left, right):
            if left == n and right == n:
                res.append(curStr)
                return
            if left < right:
                return
            if left < n:
                dfs(curStr + '(', left + 1, right)
            if right < n:
                dfs(curStr + ')', left, right + 1)

        res = []
        curStr = ''
        dfs(curStr, 0, 0)
        return res