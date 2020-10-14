# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
题解: 自顶向下做法
isBalanced(root) 函数： 判断树 root 是否平衡

特例处理： 若树根节点 root 为空，则直接返回 truetrue ；
返回值： 所有子树都需要满足平衡树性质，因此以下三者使用与逻辑 \&\&&& 连接；
abs(self.depth(root.left) - self.depth(root.right)) <= 1 ：判断 当前子树 是否是平衡树；
self.isBalanced(root.left) ： 先序遍历递归，判断 当前子树的左子树 是否是平衡树；
self.isBalanced(root.right) ： 先序遍历递归，判断 当前子树的右子树 是否是平衡树；


"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return max(left, right) + 1


