# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        # path = []
        # res = []

        def dfs(root, tar):
            if root == None:
                return False
            # path.append(root.val)
            tar -= root.val

            if tar == 0 and not root.left and not root.right:
                # path1 = path.copy()
                # res.append(path1)
                return True
            return dfs(root.left, tar) or dfs(root.right, tar)
            # path.pop()

        return dfs(root, sum)

