# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root) -> bool:
        res = []
        if root == None:
            return True

        def helper(root):
            if root == None:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        result = res.copy()
        result.sort()
        for i in range(len(result) - 1):
            if result[i] == result[i + 1]:
                return False
        if res == result:
            return True
        else:
            return False
