class Solution:
    def permute(self, nums):
        res = []

        def dfs(path, result):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(result)):
                path.append(result[i])
                dfs(path, result[:i] + result[i + 1:])
                path.pop()

        dfs([], nums)
        return res
