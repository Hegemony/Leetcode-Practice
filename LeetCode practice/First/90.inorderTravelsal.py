class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""
迭代法
"""


class Solution:
    def inorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res


"""
递归法
"""


class Solution1:
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = []
        output = []

        while stack or root:
            if root != None:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                output.append(tmp.val)
                root = tmp.right
        return output
