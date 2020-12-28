class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        q = [root]
        while q:
            l = len(q)
            tmp = []
            for i in range(l):
                r = q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                tmp.append(r.val)
            res.append(tmp)
        return res