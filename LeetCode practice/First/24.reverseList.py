# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
空间复杂度O（n）
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return
        p = head
        res = []
        while p:
            res.append(p.val)
            p = p.next
        res.reverse()
        dummpy = ListNode(' ')
        q = dummpy
        for i in range(len(res)):
            newnode = ListNode(res[i])
            q.next = newnode
            q = q.next
        return dummpy.next


"""
空间复杂度O（1）
"""
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next  # 存储后继结点
            cur.next = pre  # 修改当前next的指向
            pre = cur       # pre 暂存 cur
            cur = tmp       # cur 访问下一节点
        return pre