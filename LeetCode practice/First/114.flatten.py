class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
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
