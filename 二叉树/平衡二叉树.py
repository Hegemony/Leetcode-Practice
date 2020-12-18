class Solution:
    def isBalanced(self, root):
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return dfs(root) != -1