class Solution:
    def combinationSum2(self, candidates, target: int):
        res = []
        """
        加了一点设计，防止重复
        没有pop的dfs是dfs，不是backtrace
        在参数里传来传去，没有引用的，搞出来好多数组的。是dfs，不是backrace
        真正的回溯是从头到尾，只用了一个cur_path数组
        在参数里传来传去，不pop()都可以
        """
        def dfs(path, target, index):
            if target == 0:
                res.append(list(path))
                return
            if target < 0:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i - 1] == candidates[i]:
                    continue
                path.append(candidates[i])
                dfs(path, target - candidates[i], i + 1)
                path.pop()

        candidates.sort()
        dfs([], target, 0)
        # s = set()
        # for r in res:
        #     r.sort()
        #     if tuple(r) not in s:
        #         s.add(tuple(r))
        # result = []
        # for j in s:
        #     result.append(list(j))
        return res