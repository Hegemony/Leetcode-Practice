# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        print(left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


"""
错解
"""
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        self.max_l = 0
        self.cur_l = 0
        if root == None:
            self.max_l = 0
        self.preTraverse(root)

        return self.max_l

    def preTraverse(self, root):
        if root == None:
            return
        self.cur_l += 1
        self.preTraverse(root.left)
        self.preTraverse(root.right)
        if self.cur_l > self.max_l:
            self.max_l = self.cur_l

# 0
# 1
# 0
# 1
# 0
#
# 0
# 0
# 1
# 0
# 0
# 1
# 0
# 0
# 1
# 2
#
# 0
# 0
# 0
# 1
# 2
