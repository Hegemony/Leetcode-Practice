# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
第一种递归思路，先序遍历，先调换左右子树，再分别对叶子结点进行调换。
"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 递归函数的终止条件，节点为空时返回
        if not root:
            return None
        # 将当前节点的左右子树交换
        root.left, root.right = root.right, root.left
        # 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 函数返回时就表示当前这个节点，以及它的左右子树
        # 都已经交换完了
        return root


"""
第二种递归思路，后序遍历，先把叶子结点左右调换，再一层层向上。
"""
class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

