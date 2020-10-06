# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
中序遍历，存储结果到两个数组，
反转其中一个数组，结果出错。
"""
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        tree1, tree2 = root.left, root.right
        nums1, nums2 = [], []
        self.leftsearch(tree1, nums1)
        self.rightsearch(tree2, nums2)
        print(nums1)
        print(nums2)
        nums2.reverse()
        return nums1 == nums2

    def leftsearch(self, tree, nums):
        # print(tree.val)
        if tree == None:
            return

        # if not tree.left and not tree.right:
        #     return
        self.leftsearch(tree.left, nums)
        nums.append(tree.val)
        self.leftsearch(tree.right, nums)

    def rightsearch(self, tree, nums):
        # print(tree.val)
        if tree == None:
            return

        # if not tree.left and not tree.right:
        #     return
        self.rightsearch(tree.left, nums)
        nums.append(tree.val)
        self.rightsearch(tree.right, nums)

a, b, c, d, e, f, g = TreeNode(1), TreeNode(2), TreeNode(2), TreeNode('null'), TreeNode(3), TreeNode('null'), TreeNode(3)
a.left, a.right, b.left, b.right, c.left, c.right = b, c, d, e, f, g

print(Solution2().isSymmetric(a))