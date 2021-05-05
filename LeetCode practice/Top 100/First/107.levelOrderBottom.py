# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        res = []
        if not root:
            return []
        q = [root]
        while q:
            r = []
            for i in range(len(q)):
                tmp = q.pop(0)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
                r.append(tmp.val)
            res.append(r)
        res.reverse()
        return res