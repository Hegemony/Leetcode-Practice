class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        递归写法
        """
        def dfs(root, low, high):
            if not root:
                return True
            val = root.val
            if val <= low or val >= high:
                return False
            if not dfs(root.left, low, root.val):
                return False
            if not dfs(root.right, root.val, high):
                return False
            return True

        return dfs(root, float('-inf'), float('inf'))

        # """
        # 中序遍历
        # """
        # res = []

        # def dfs(root):
        #     if root == None:
        #         return
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # for i in range(len(res) - 1):
        #     if res[i] >= res[i + 1]:
        #         return False
        # return True