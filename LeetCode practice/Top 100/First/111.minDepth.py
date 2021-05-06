# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
本题也可以理解为从叶子节点到根节点的最短路径，可以采用自底向上的后序遍历递归。
需要注意的是，某一节点只有左子树或者只有右子树的话那么该节点的最小深度就是它的左子树或者右子树的最小深度加一
"""


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right + 1
        if right == 0:
            return left + 1
        return min(left, right) + 1
