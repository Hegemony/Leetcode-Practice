class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if i < 10 and j < 10:
        #             if i + j <= k:
        #                 res += 1
        #         if i >= 10 and j >= 10:
        #             tmp_i1 = i % 10
        #             tmp_i2 = i // 10
        #
        #             tmp_j1 = j % 10
        #             tmp_j2 = j // 10
        #             if tmp_i1 + tmp_i2 + tmp_j1 + tmp_j2 <= k:
        #                 res += 1
        #         if i >= 10 and j < 10:
        #             tmp_i1 = i % 10
        #             tmp_i2 = i // 10
        #             if tmp_i1 + tmp_i2 + j <= k:
        #                 res += 1
        #         if i < 10 and j >= 10:
        #             tmp_j1 = j % 10
        #             tmp_j2 = j // 10
        #             if i + tmp_j1 + tmp_j2 <= k:
        #                 res += 1
        return


"""
题解：递推解法
"""


class Solution1:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def digitsum(n):
            ans = 0
            while n != 0:
                ans += n % 10
                n = n // 10
            return ans

        vis = set()
        vis.add((0, 0))
        # vis = set([(0,0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))

        return len(vis)


# print(Solution1().movingCount(12, 8, 4))

"""
题解：DFS解法
"""


class Solution2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def digits(n):
            ans = 0
            while n != 0:
                ans += n % 10
                n = n // 10
            return ans

        def dfs(i, j):
            if i >= m or j >= n or k < digits(i) + digits(j) or (i, j) in visited:
                return 0
            visited.add((i, j))
            # print(visited)
            # return 1 + dfs(i + 1, j) + dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        visited = set()
        dfs(0, 0)
        return len(visited)


print(Solution2().movingCount(12, 8, 4))