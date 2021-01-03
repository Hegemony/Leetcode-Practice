class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        一次递归
        """

        def dfs(p, q):
            if p == None and q == None:
                return True
            if not p and not q:
                return False
            return p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)

        # 两次递归

        # res1 = []
        # res2 = []
        #
        # def dfs1(root):
        #     if not root:
        #         res1.append('#')
        #         return
        #     res1.append(root.val)
        #     dfs1(root.left)
        #     dfs1(root.right)
        #
        # def dfs2(root):
        #     if not root:
        #         res2.append('#')
        #         return
        #     res2.append(root.val)
        #     dfs2(root.left)
        #     dfs2(root.right)
        #
        # dfs1(p)
        # dfs2(q)
        # return res1 == res2