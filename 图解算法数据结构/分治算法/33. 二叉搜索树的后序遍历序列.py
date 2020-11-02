class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verifyPostorder(self, postorder) -> bool:
        inorder = postorder.copy()
        inorder.sort()

        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            if len(postorder) > 0:
                val = postorder.pop()
                root = TreeNode(val)
                index = idx_map[val]

                root.right = helper(index + 1, in_right)

                root.left = helper(in_left, index - 1)
                return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        r = helper(0, len(inorder) - 1)
        res = []

        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(r)
        if res == inorder:
            return True
        else:
            return False


print(Solution().verifyPostorder([1, 2, 5, 10, 6, 9, 4, 3]))

"""
题解
"""
class Solution1:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
