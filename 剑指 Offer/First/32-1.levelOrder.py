# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        while q:
            tmp = q.pop(0)
            if tmp.left != None:
                q.append(tmp.left)
            if tmp.right != None:
                q.append(tmp.right)
            res.append(tmp.val)
        return res