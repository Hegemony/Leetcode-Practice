# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
题解做法
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)  # 递归得到结果直接return
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)  # 递归得到结果直接return
            # print(root.val)
        return root
