# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if root == None:
            return []
        path = []
        res = []
        def dfs(root, tar):
            if root == None:
                return
            path.append(root.val)
            tar -= root.val

            if tar == 0 and root.left == None and root.right == None:
                """
                以 Python 语言为例，记录路径时若直接执行 res.append(path) ，则是将此 path 对象加入了 res ；后续 path 改变时， 
                res 中的 path 对象也会随之改变，因此无法实现结果记录。正确做法为：拷贝到一个新的列表里
                """
                path1 = path.copy()
                res.append(path1)
                # res.append(list(path))
            dfs(root.left, tar)
            dfs(root.right, tar)
            path.pop()

        dfs(root, sum)
        return res