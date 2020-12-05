# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        tmp = []
        def dfs(root, sum):
            if not root:
                return
            tmp.append(root.val)  # 先序遍历遇到节点就添加进来
            sum -= root.val
            if sum == 0 and not root.left and not root.right:
                res.append(list(tmp))   # 这里一定要list(tmp)，否则后续tmp改变，整个res里面的值也会改变
            # print('tmp', tmp, 'res', res, 'sum', sum)
            dfs(root.left, sum)
            dfs(root.right, sum)
            tmp.pop()             # 回溯的时候，在先序遍历结束就删除刚才的节点
        dfs(root, sum)
        return res