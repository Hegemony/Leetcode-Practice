# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1.递归解决前序遍历
"""
class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        def dfs(root):
            if root == None:
                return None
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res


"""
1.迭代法解决前序遍历:
从根节点开始，每次迭代弹出当前栈顶元素，并将其孩子节点压入栈中，先压右孩子再压左孩子。
在这个算法中，输出到最终结果的顺序按照 Top->Bottom 和 Left->Right，符合前序遍历的顺序。
"""
class Solution1:
    def preorderTraversal(self, root: TreeNode):
        if root == None:
            return []
        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            if root != None:
                output.append(root.val)
                if root.right != None:
                    stack.append(root.right)
                if root.left != None:
                    stack.append(root.left)
        return output


"""
2.递归解决中序遍历
"""
class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        def dfs(root):
            if root == None:
                return None
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res


"""
2.迭代解决中序遍历
"""
class Solution1:
    def inorderTraversal(self, root: TreeNode):
        """
    	:type root: TreeNode
		:rtype: List[int]
    	"""
        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res


"""
3.递归解决后序遍历
"""
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        def dfs(root):
            if root == None:
                return None
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res


"""
3.迭代解决后序遍历
"""
class Solution1:
    def postorderTraversal(self, root: TreeNode):
        """
        相比较前序遍历，仅仅改变了left 和 right的顺序：
        所以本题思路将会是：在前序遍历中，把left 和 right的顺序调换，然后输出反转的树即可。
        :param root:
        :return:
        """
        if root == None:
            return []
        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            if root != None:
                output.append(root.val)
                if root.left != None:
                    stack.append(root.left)
                if root.right != None:
                    stack.append(root.right)
        output.reverse()
        return output


"""
4.二叉树的层序遍历
"""
class Solution:
    def levelOrder(self, root: TreeNode):
        res = []
        # 如果根节点为空，则返回空列表
        if root == None:
            return res
        # 模拟一个队列存储节点
        q = []
        # 将首节点入队
        q.append(root)

        # 列表为空时，循环结束
        while q:
            l = len(q)
            tmp = []
            for i in range(l):
                r = q.pop(0)
                if r.left != None:
                    q.append(r.left)
                if r.right != None:
                    q.append(r.right)
                tmp.append(r.val)
            res.append(tmp)
        return res