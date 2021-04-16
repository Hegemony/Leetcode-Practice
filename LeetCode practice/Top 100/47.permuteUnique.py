class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()

        def dfs(path, result):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(result)):
                if i > 0 and result[i] == result[i - 1]:
                    continue
                path.append(result[i])
                dfs(path, result[:i] + result[i + 1:])
                path.pop()

        dfs([], nums)
        return res
