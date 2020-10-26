# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
先序遍历树 A 中的每个节点 nA ；（对应函数 isSubStructure(A, B)）
判断树 A 中 以 nA为根节点的子树 是否包含树 B 。（对应函数 helper(A, B)）

helper(A, B) 函数：
终止条件：
当节点 B 为空：说明树 B 已匹配完成（越过叶子节点），因此返回 true ；
当节点 A 为空：说明已经越过树 A 叶子节点，即匹配失败，返回 false ；
当节点 A 和 B 的值不同：说明匹配失败，返回 false ；
返回值：
判断 A 和 B 的左子节点是否相等，即 helper(A.left, B.left) ；
判断 A 和 B 的右子节点是否相等，即 helper(A.right, B.right) ；

isSubStructure(A, B) 函数：
特例处理： 当 树 A 为空 或 树 B 为空 时，直接返回 false ；
返回值： 若树 B 是树 A 的子结构，则必满足以下三种情况之一，因此用或 || 连接；
以 节点 A 为根节点的子树 包含树 B ，对应 helper(A, B)；
树 B 是 树 A 左子树 的子结构，对应 isSubStructure(A.left, B)；
树 B 是 树 A 右子树 的子结构，对应 isSubStructure(A.right, B)

"""
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        res = False
        if A is not None and B is not None:
            if A.val == B.val:
                res = self.helper(A, B)
            if not res:
                res = self.isSubStructure(A.left, B)
            if not res:
                res = self.isSubStructure(A.right, B)
        return res

    def helper(self, A, B):
        if B is None:
            return True
        if A is None:
            return False
        if A.val != B.val:
            return False
        return self.helper(A.left, B.left) and self.helper(A.right, B.right)


# class Solution:
#     def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
#         def recur(A, B):
#             if not B:
#                 return True
#             if not A or A.val != B.val:
#                 return False
#             return recur(A.left, B.left) and recur(A.right, B.right)
#
#         return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

