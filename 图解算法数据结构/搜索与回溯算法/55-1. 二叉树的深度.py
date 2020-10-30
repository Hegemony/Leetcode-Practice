# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(root):
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            print(left, right)
            return max(left, right) + 1
        return depth(root)