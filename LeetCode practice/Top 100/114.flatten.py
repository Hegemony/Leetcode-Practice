# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
题解：
具体做法是，对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，
将当前节点的右子节点赋给前驱节点的右子节点，然后将当前节点的左子节点赋给当前节点的右子节点，
并将当前节点的左子节点设为空。对当前节点处理结束后，继续处理链表中的下一个节点，直到所有节点都处理结束。
"""


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                nxt = curr.left    # 先找一个左节点
                pre = nxt
                while pre.right:   # 找到左子树最右侧的节点
                    pre = pre.right
                pre.right = curr.right   # 将curr的右侧所有节点给左子树最右侧节点的右节点，此时节点在左子树保存在nxt
                curr.left = None         # 删掉左子树
                curr.right = nxt         # 将nxt给curr的右子树
            curr = curr.right            # while的循环
