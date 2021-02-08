# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        self.res += self.helper(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.res

    def helper(self, root, sum):
        if root == None:
            return []
        path = []
        res = []

        def dfs(root, tar):
            if root == None:
                return
            path.append(root.val)
            tar -= root.val
            if tar == 0:
                path1 = path.copy()
                res.append(path1)
            dfs(root.left, tar)
            dfs(root.right, tar)
            path.pop()

        dfs(root, sum)
        return len(res)
