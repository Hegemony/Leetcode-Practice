# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val and self.dfs(l.left, r.left) and self.dfs(l.right, r.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.dfs(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
