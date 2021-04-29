# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        递归写法
        """
        def dfs(root, low, high):
            if not root:
                return True
            val = root.val
            if val <= low or val >= high:
                return False
            if not dfs(root.left, low, root.val):
                return False
            if not dfs(root.right, root.val, high):
                return False
            return True

        return dfs(root, float('-inf'), float('inf'))
