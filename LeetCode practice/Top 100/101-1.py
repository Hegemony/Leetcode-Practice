# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
正解：
左子树左（右）节点 == 右子树右（左）节点
根左右               根右左
先序遍历
"""
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        tree1, tree2 = root.left, root.right
        nums1, nums2 = [], []
        self.leftsearch(tree1, nums1)
        self.rightsearch(tree2, nums2)
        print(nums1)
        print(nums2)
        return nums1 == nums2

    def leftsearch(self, tree, nums):
        # print(tree.val)
        if tree == None:
            nums.append('')   # 如果该节点为空，需要用空串占位
            return
        nums.append(tree.val)
        print(nums)
        # if not tree.left and not tree.right:
        #     return
        self.leftsearch(tree.left, nums)
        self.leftsearch(tree.right, nums)

    def rightsearch(self, tree, nums):
        # print(tree.val)
        if tree == None:
            nums.append('')  # 如果该节点为空，需要用空串占位
            return
        nums.append(tree.val)
        print(nums)
        # if not tree.left and not tree.right:
        #     return
        self.rightsearch(tree.right, nums)
        self.rightsearch(tree.left, nums)


a, b, c, d, e, f, g = TreeNode(1), TreeNode(2), TreeNode(2), TreeNode('null'), TreeNode(3), TreeNode('null'), TreeNode(3)
a.left, a.right, b.left, b.right, c.left, c.right = b, c, d, e, f, g

print(Solution1().isSymmetric(a))