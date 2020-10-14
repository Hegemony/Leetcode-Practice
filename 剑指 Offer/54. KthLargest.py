# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def preTraversal(root, nums):
            if root == None:
                return
            nums.append(root.val)
            preTraversal(root.left, nums)
            preTraversal(root.right, nums)
        nums = []
        preTraversal(root, nums)
        nums.sort(reverse=True)
        return nums[k-1]