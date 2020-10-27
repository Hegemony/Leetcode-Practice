# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # nums = []
        if root == None:
            return
        left, right = self.mirrorTree(root.left), self.mirrorTree(root.right)
        root.left, root.right = right, left
        return root

        # def dfs(root):
        #     if root == None:
        #         return
        #     nums.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)