# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
            l = len(q)
            tmp = []
            for i in range(l):  # 看队列长度，长度代表每层的节点数量
                r = q.pop(0)
                if r.left != None:
                    q.append(r.left)
                if r.right != None:
                    q.append(r.right)
                tmp.append(r.val)
            res.append(tmp)
        return res
