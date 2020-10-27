# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if root == None:
            return []
        result = []
        q = [root]

        while q:
            l = len(q)
            res = []
            for i in range(l):
                tmp = q.pop(0)
                res.append(tmp.val)
                if tmp.left != None:
                    q.append(tmp.left)
                if tmp.right != None:
                    q.append(tmp.right)
            result.append(res)
        return result