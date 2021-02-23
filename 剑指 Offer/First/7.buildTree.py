# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            tmp = preorder.pop(0)
            index = idx_map[tmp]
            root = TreeNode(tmp)
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)
            return root
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        n = len(inorder)
        return helper(0, n - 1)