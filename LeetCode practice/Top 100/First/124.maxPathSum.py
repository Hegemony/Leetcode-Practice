# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = float('-inf')

        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.maxsum = max(self.maxsum, left + right + root.val)
            return max(left, right) + root.val

        dfs(root)
        return self.maxsum