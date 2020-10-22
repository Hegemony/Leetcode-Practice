# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
求二叉树的深度
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        def depth(root):
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left, right) + 1
        left = depth(root.left)
        right = depth(root.right)
        return max(left, right) + 1


"""
求二叉树的深度的简洁写法：
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


"""
递归求解是否为对称二叉树
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        res1 = []
        res2 = []
        def leftsearch(root):
            if root == None:
                res1.append(' ')
                return
            res1.append(root.val)
            leftsearch(root.left)
            leftsearch(root.right)
        def rightsearch(root):
            if root == None:
                res2.append(' ')
                return
            res2.append(root.val)
            rightsearch(root.right)
            rightsearch(root.left)

        leftsearch(root.left)
        rightsearch(root.right)
        return res1 == res2


"""
广度优先搜索求解二叉树路径和
"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        p = [root]      # 存储节点
        q = [root.val]  # 存储节点的累加和

        while p:
            tmp = p.pop(0)
            res = q.pop(0)
            if tmp.left == None and tmp.right == None:
                if res == sum:
                    return True
            if tmp.left != None:
                p.append(tmp.left)
                q.append(res + tmp.left.val)
            if tmp.right != None:
                p.append(tmp.right)
                q.append(res + tmp.right.val)
        return False
