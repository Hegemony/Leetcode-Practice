# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def helper(i, j):
            if i > j:
                return
            tmp = preorder.pop(0)
            p = idx_map[tmp]
            root = TreeNode(tmp)
            root.left = helper(i, p - 1)
            root.right = helper(p + 1, j)
            return root
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
