# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
从中序与后序遍历序列构造二叉树：
（从后序中取出元素，然后在中序数组中进行构建）

为了高效查找根节点元素在中序遍历数组中的下标，我们选择创建哈希表来存储中序序列，即建立一个（元素，下标）键值对的哈希表。

定义递归函数 helper(in_left, in_right) 表示当前递归到中序序列中当前子树的左右边界，递归入口为helper(0, n - 1) ：

如果 in_left > in_right，说明子树为空，返回空节点。

选择后序遍历的最后一个节点作为根节点。

利用哈希表 O(1)查询当根节点在中序遍历中下标为 index。从 in_left 到 index - 1 属于左子树，从 index + 1 到 in_right 属于右子树。

根据后序遍历逻辑，递归创建右子树 helper(index + 1, in_right) 和左子树 helper(in_left, index - 1)。
注意这里有需要先创建右子树，再创建左子树的依赖关系。可以理解为在后序遍历的数组中整个数组是先存储左子树的节点，再存储右子树的节点，最后存储根节点，
如果按每次选择「后序遍历的最后一个节点」为根节点，则先被构造出来的应该为右子树。

返回根节点 root
"""


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def helper(in_left, in_right):
            # 如果没有节点构造二叉树，就结束
            if in_left > in_right:
                return None
            # 后序遍历的最后的元素，作为子树的根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据root所在中序数组的位置分成左右两棵子树
            index = idx_map[val]

            # 构造右子树
            root.right = helper(index + 1, in_right)

            # 构造左子树
            root.left = helper(in_left, index - 1)
            return root

        # 建立（元素， 下标）键值对的哈希表
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


print(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))

"""
从前序与中序遍历序列构造二叉树：
（从前序中取出元素，然后在中序数组中进行构建）
根据后序遍历逻辑，递归创建左子树helper(in_left, index - 1) 和右子树 helper(index + 1, in_right)
注意这里有需要先创建左子树，再创建右子树的依赖关系。可以理解为在前序序遍历的数组中整个数组是先存储根节点，再存储左子树的节点，最后存储右子树的节点，
如果按每次选择「前序遍历的最后一个节点」为根节点，则先被构造出来的应该为左子树。
"""

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def helper(in_left, in_right):
            # 如果没有节点构造二叉树，就结束
            if in_left > in_right:
                return None
            # 前序遍历的最后的元素，作为子树的根节点
            val = preorder.pop(0)
            index = idx_map[val]

            # 根据root所在中序数组的位置分成左右两棵子树
            root = TreeNode(val)

            # 构建左子树
            root.left = helper(in_left, index - 1)
            # 构建右子树
            root.right = helper(index + 1, in_right)
            return root

        # 建立（元素， 下标）键值对的哈希表
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(preorder) - 1)
