# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.pre:
                self.pre.right = root
                root.left = self.pre
            else:
                self.head = root
            self.pre = root
            dfs(root.right)

        if not root:
            return
        self.pre = None
        self.head = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head