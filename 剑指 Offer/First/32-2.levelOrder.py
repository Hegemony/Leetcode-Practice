# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        q = []
        q.append(root)
        res = []
        while q:
            tmp = []
            for i in range(len(q)):
                r = q.pop(0)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
                tmp.append(r.val)
            res.append(tmp)
        return res