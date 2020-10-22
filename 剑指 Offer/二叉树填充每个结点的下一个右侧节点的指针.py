"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
填充完美二叉树的右侧节点指针
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return
        p = [root]

        while len(p) > 0:
            n = len(p)
            q = []
            for i in range(n):
                tmp = p.pop(0)
                q.append(tmp)
                if tmp.left != None:
                    p.append(tmp.left)
                if tmp.right != None:
                    p.append(tmp.right)
            for i in range(len(q)):
                if i == len(q) - 1:
                    q[i].next = None
                else:
                    q[i].next = q[i+1]
        return root


"""
填充二叉树的右侧节点指针
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return
        p = [root]

        while len(p) > 0:
            n = len(p)
            q = []
            for i in range(n):
                tmp = p.pop(0)
                q.append(tmp)
                if tmp.left != None:
                    p.append(tmp.left)
                if tmp.right != None:
                    p.append(tmp.right)
            for i in range(len(q)):
                if i == len(q) - 1:
                    q[i].next = None
                else:
                    q[i].next = q[i+1]
        return root


"""
输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

"""