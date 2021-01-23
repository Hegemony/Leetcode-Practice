# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        cnt = 1
        while q:
            tmp = []
            if cnt % 2 == 1:
                for i in range(len(q)):
                    root = q.pop(0)
                    if root.left:
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)
                    tmp.append(root.val)
            elif cnt % 2 == 0:
                for i in range(len(q)):
                    root = q.pop(0)
                    if root.left:
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)
                    tmp.append(root.val)
                tmp.reverse()
            res.append(tmp)
            cnt += 1
        return res