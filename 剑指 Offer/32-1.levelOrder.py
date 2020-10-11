# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
二叉树的广度优先搜索
"""
class Solution:
    def levelOrder(self, root: TreeNode):
        res = []
        # 如果根节点为空，则返回空列表
        if root == None:
            return res
        # 模拟一个队列存储节点
        q = []
        # 将首节点入队
        q.append(root)

        # 列表为空时，循环结束
        while len(q) > 0:
            r = q.pop(0)
            if r.left != None:
                q.append(r.left)
            if r.right != None:
                q.append(r.right)
            res.append(r.val)
        return res