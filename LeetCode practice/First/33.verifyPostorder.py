class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verifyPostorder(self, postorder) -> bool:
        def dfs(i, j):
            print(i, j)
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and dfs(i, m - 1) and dfs(m, j - 1)

        return dfs(0, len(postorder) - 1)


print(Solution().verifyPostorder([1, 2, 5, 10, 6, 9, 4, 3]))
