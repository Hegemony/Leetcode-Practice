# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        res = []
        if not root:
            return []
        q = [root]
        while q:
            r = []
            l = len(q)
            # res.append(tmp.val)
            for i in range(l):
                tmp = q.pop(0)
                r.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            res.append(r)
        return res