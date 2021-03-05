# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left)
        if not root:
            return True
        return dfs(root.left, root.right)

