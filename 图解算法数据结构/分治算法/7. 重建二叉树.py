# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = preorder.pop(0)
            index = idx_map[val]
            root = TreeNode(val)
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            return root
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)