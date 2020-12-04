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
        while q:
            r = q.pop(0)
            res.append(r.val)
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        return res