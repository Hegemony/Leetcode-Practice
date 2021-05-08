# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                nxt = curr.left
                pre = nxt
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
