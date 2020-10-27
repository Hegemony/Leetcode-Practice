# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        nums1 = []
        nums2 = []
        self.leftdfs(root.left, nums1)
        self.rightdfs(root.right, nums2)
        return nums1 == nums2

    def leftdfs(self, root, nums1):
        if root == None:
            nums1.append(' ')
            return
        nums1.append(root.val)
        self.leftdfs(root.left, nums1)
        self.leftdfs(root.right, nums1)

    def rightdfs(self, root, nums2):
        if root == None:
            nums2.append(' ')
            return
        nums2.append(root.val)
        self.rightdfs(root.right, nums2)
        self.rightdfs(root.left, nums2)

