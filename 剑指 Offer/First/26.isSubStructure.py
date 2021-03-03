# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A and not B:
            return True

        if not A or not B:
            return False

        def dfs(s, t):
            if not t:
                return True
            if not s:
                return False
            return s.val == t.val and dfs(s.left, t.left) and dfs(s.right, t.right)

        return dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)