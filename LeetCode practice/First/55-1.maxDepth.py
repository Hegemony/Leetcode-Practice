# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if root == None:
        #     return 0
        # q = []
        # q.append(root)
        # depth = 0
        # while q:
        #     l = len(q)
        #     for i in range(l):
        #         r = q.pop(0)
        #         if r.left:
        #             q.append(r.left)
        #         if r.right:
        #             q.append(r.right)
        #     depth += 1
        # return depth
        if root == None:
            return 0

        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return max(left, right) + 1  # 后序遍历返回子树高度

        return dfs(root)