# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode):
        if root == None:
            return []
        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            if root != None:
                output.append(root.val)
                if root.left != None:
                    stack.append(root.left)
                if root.right != None:
                    stack.append(root.right)
        output.reverse()
        return output
