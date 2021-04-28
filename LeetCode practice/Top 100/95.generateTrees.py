# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        def dfs(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end + 1):
                # 获得所有可行的左子树集合
                leftTrees = dfs(start, i - 1)

                # 获得所有可行的右子树集合
                rightTrees = dfs(i + 1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees
        return dfs(1, n) if n else []
