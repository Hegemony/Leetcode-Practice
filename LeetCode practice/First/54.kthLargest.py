# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        nums = []
        def dfs(root):
           if root == None:
               return
           dfs(root.left)
           nums.append(root.val)
           dfs(root.right)
        dfs(root)
        nums.reverse()
        return nums[k - 1]
