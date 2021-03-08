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
        cnt = 0
        while q:
            tmp = []
            cnt += 1
            for i in range(len(q)):
                r = q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                tmp.append(r.val)
            if cnt % 2 == 1:
                res.append(tmp)
            else:
                tmp.reverse()
                res.append(tmp)
        return res