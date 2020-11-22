# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        res = []
        if root == None:
            return res
        q = []
        q.append(root)

        while q:
            l = len(q)
            tmp = []
            for i in range(l):
                r = q.pop(0)
                if r.left != None:
                    q.append(r.left)
                if r.right != None:
                    q.append(r.right)
                tmp.append(r.val)
            res.append(tmp)
        return res
