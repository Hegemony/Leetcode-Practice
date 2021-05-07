# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if root == None:
            return []
        path = []
        res = []

        def dfs(root, tar):
            if root == None:
                return
            path.append(root.val)
            tar -= root.val

            if tar == 0 and root.left == None and root.right == None:
                path1 = path.copy()
                res.append(path1)
            dfs(root.left, tar)
            dfs(root.right, tar)
            path.pop()

        dfs(root, sum)
        return res
