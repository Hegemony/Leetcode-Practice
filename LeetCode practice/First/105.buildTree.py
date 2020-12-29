class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        def helper(i, j):
            if i > j:
                return
            tmp = preorder.pop(0)
            idx = idx_map[tmp]
            root = TreeNode(tmp)
            root.left = helper(i, idx - 1)
            root.right = helper(idx + 1, j)
            return root
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        helper(0, len(inorder) - 1)
