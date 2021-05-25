# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode):
        if not root:
            return []
            # 第一想法是哈希表记录
        Hash = {}

        def dfs(root, Hash):
            if not root:
                return
            Hash[root.val] = Hash.get(root.val, 0) + 1
            dfs(root.left, Hash)
            dfs(root.right, Hash)

        dfs(root, Hash)
        mode = max(Hash.values())
        return [key for key in Hash.keys() if Hash[key] == mode]