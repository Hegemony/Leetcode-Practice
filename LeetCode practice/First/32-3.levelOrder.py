# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = []
        q = []
        q.append(root)
        cnt = 1
        while len(q):
            tmp = []
            if cnt % 2 == 1:
                for i in range(len(q)):
                    r = q.pop(0)
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
                    tmp.append(r.val)
            if cnt % 2 == 0:
                for i in range(len(q)):
                    r = q.pop(0)
                    if r.left:
                        q.append(r.left)
                    if r.right:
                        q.append(r.right)
                    tmp.append(r.val)
                tmp.reverse()
            res.append(tmp)
            cnt += 1
        return res