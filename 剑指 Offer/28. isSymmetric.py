# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        left = root.left
        right = root.right
        num1 = []
        num2 = []
        self.leftsearch(left, num1)
        self.rightsearch(right, num2)
        num2.reverse()
        return num1 == num2

    def leftsearch(self, root, num1):
        if root == None:
            num1.append(' ')
            return
        num1.append(root.val)
        self.leftsearch(root.left, num1)
        self.leftsearch(root.right, num1)

    def rightsearch(self, root, num2):
        if root == None:
            num2.append(' ')
            return
        num2.append(root.val)
        self.rightsearch(root.left, num2)
        self.rightsearch(root.right, num2)