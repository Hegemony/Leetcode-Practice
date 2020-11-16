"""
深度优先+剪枝，速度19%
"""


class Solution:
    def combinationSum(self, candidates, target: int):
        candidates = sorted(candidates)

        def helper(s, use, index):
            if s == target:
                res.append(use)
                return
            if s > target:
                return

            for i in range(index, len(candidates)):
                c = candidates[i]
                helper(s + c, use + [c], i)

        use, res = [], []
        index = 0
        helper(0, use, index)
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))

"""
题解：96%
变量意义：use表示已经使用过的数（组成的列表），remain表示距离target还有多大。
"""


class Solution1:
    def combinationSum(self, candidates, target: int):
        candidates = sorted(candidates)

        ans = []

        def find(s, use, remain):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain:
                    ans.append(use + [c])
                if c < remain:
                    find(i, use + [c], remain - c)
                if c > remain:
                    return

        find(0, [], target)
        return ans
