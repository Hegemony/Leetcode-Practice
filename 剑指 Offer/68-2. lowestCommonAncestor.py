# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
递归解析：
终止条件：
当越过叶节点，则直接返回 null ；
当 root等于 p, q ，则直接返回 root ；
递推工作：
开启递归左子节点，返回值记为 left ；
开启递归右子节点，返回值记为 right ；
返回值： 根据 left 和 right ，可展开为四种情况；
1.当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q ，返回 null ；
2.当 left和 right 同时不为空 ：说明 p, q 分列在 root的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root ；
3.当 left为空 ，right 不为空 ：p,q 都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：
(1)p,q 其中一个在 root 的 右子树 中，此时 right 指向 p（假设为 p ）；
(2)p,q 两节点都在 root 的 右子树 中，此时的 right指向 最近公共祖先节点 ；
4.当 left不为空 ， right为空 ：与情况 3. 同理；
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:   # 1.
            return
        if not left:       # 3.
            return right
        if not right:      # 4.
            return left
        return root        # 2. if left and right:
