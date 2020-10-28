# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return
        res = []
        def dfs(cur):
            if cur == None:
                return
            dfs(cur.left)
            res.append(root.val)
            self.pre = cur
            dfs(cur.right)

        dfs(root)
        head = Node
        head.left = None
        p = head
        p.right = Node(res[0])
        p = p.right
        for i in range(1, len(res)):
            if i == len(res) - 1:
                p.left = Node(res[i - 1])
                p.right = Node(res[0])

            p.left = Node(res[i-1])
            p.right = Node(res[i])
            p = p.right
        return head



class Solution1:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return
        def dfs(cur):   # 进行中序遍历
            if cur == None:
                return
            dfs(cur.left)   # 递归左子树

            if self.pre:    # 修改节点引用
                self.pre.right = cur
                cur.left = self.pre
            else:
                self.head = cur    # 记录头节点
            self.pre = cur   # 保存 cur

            dfs(cur.right)   # 递归右子树

        self.head = None
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return

        def dfs(cur):
            if cur == None:
                return
            dfs(cur.left)
            if self.pre != None:
                self.pre.right = cur
                cur.left = self.pre
            if self.pre == None:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        self.pre = None
        self.head = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head

