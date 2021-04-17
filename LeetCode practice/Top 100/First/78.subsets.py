class Solution:
    def subsets(self, nums):
        res = [[]]

        def dfs(path, result):
            res.append(list(path))
            for i in range(len(result)):
                path.append(result[i])
                dfs(path, result[i + 1:])
                path.pop()

        dfs([], nums)
        return res


print(Solution().subsets([1, 2, 3]))
