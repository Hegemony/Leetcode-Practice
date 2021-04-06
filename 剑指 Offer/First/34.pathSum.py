# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, target: int):
        path = []
        tmp = []

        def helper(root, target):
            if not root:
                return
            tmp.append(root.val)  # 全局变量先加入
            target -= root.val  # 内部变量每次递归的时候都有自己的固定的值
            if target == 0 and not root.left and not root.right:
                path.append(list(tmp))
            helper(root.left, target)
            helper(root.right, target)
            tmp.pop()  # 全局变量后删除

        helper(root, target)
        return path

