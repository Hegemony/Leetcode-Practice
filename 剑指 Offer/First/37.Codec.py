# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        q = []
        q.append(root)
        res = []
        while q:
            tmp = q.pop(0)
            if tmp:
                res.append(str(tmp.val))
                q.append(tmp.left)
                q.append(tmp.right)
            else:
                res.append('null')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = data.split(',')
        i = 0
        q = []
        if res[i] == 'null':
            return
        root = TreeNode(res[i])
        q.append(root)
        while q:
            r = q.pop(0)
            i += 1
            if res[i] != 'null':
                r.left = TreeNode(int(res[i]))
                q.append(r.left)
            i += 1
            if res[i] != 'null':
                r.right = TreeNode(int(res[i]))
                q.append(r.right)
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
