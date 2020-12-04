# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
匹配类二叉树模板
"""


class Solution:
    def dfs(self, l, r):
        if not l and not r:    # 原树和子结构同时到达null
            return True
        if not l or not r:     # 原树和子结构其中一个先到达null
            return False
        return l.val == r.val and self.dfs(l.left, r.left) and self.dfs(l.right, r.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A and not B:
            return True
        if not A or not B:
            return False

        return self.dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


"""
当节点 B 为空：说明树 B 已匹配完成（越过叶子节点），因此返回 true ；
当节点 A 为空：说明已经越过树 A 叶子节点，即匹配失败，返回 false ；
当节点 A 和 B 的值不同：说明匹配失败，返回 false ；
"""


class Solution1:
    def dfs(self, l, r):
        if not r:  # 子结构到达null
            return True
        if not l:  # 原树先到null，则没有匹配到
            return False
        return l.val == r.val and self.dfs(l.left, r.left) and self.dfs(l.right, r.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False

        return self.dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
