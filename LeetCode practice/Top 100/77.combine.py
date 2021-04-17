class Solution:
    def combine(self, n: int, k: int):
        nums = [i + 1 for i in range(n)]
        res = []

        def dfs(path, result):
            if len(path) == k:
                res.append(list(path))
                return
            for i in range(len(result)):
                path.append(result[i])
                print(path)
                dfs(path, result[i + 1:])
                path.pop()
        dfs([], nums)
        return res


print(Solution().combine(4, 2))
