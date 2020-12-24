class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        self.summ = 0
        self.dfs(root)
        return root

    def dfs(self, root):  # 中序的逆过程
        if not root:
            return
        self.dfs(root.right)
        self.summ += root.val
        root.val = self.summ
        self.dfs(root.left)
