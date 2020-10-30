# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left, right) + 1

        if abs(depth(root.left) - depth(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if root == None:
                return 0
            left = depth(root.left)
            if left == -1:    # 只要有一棵子树深度为-1，他的根节点就是-1
                return -1
            right = depth(root.right)
            if right == -1:   # 只要有一棵子树深度为-1，他的根节点就是-1
                return -1
            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                return -1

        return depth(root) != -1