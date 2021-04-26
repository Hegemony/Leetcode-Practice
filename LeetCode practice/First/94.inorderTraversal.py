# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        """
        递归法
        """
        # res = []
        #
        # def helper(root):
        #     if not root:
        #         return
        #     helper(root.left)
        #     res.append(root.val)
        #     helper(root.right)
        #
        # helper(root)
        # return res
        """
        迭代法
        """
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