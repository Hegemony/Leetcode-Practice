class Solution:
    def combinationSum(self, candidates, target: int):
        res = []

        def dfs(path, target, index):
            # if sum(path) == target:
            if target == 0:
                res.append(list(path))
                return
            # if sum(path) > target:
            if target < 0:
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(path, target - candidates[i], i)
                path.pop()

        dfs([], target, 0)
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
