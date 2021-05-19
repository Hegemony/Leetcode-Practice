# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            if root != None:
                output.append(root.val)
                if root.right != None:
                    stack.append(root.right)
                if root.left != None:
                    stack.append(root.left)
        return output
