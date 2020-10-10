# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
暴力遍历，然后创建链表
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1 == None and l2 == None:
            return
        p = l1
        q = l2
        res = []
        while p:
            res.append(p.val)
            p = p.next
        while q:
            res.append(q.val)
            q = q.next
        res.sort()

        head = ListNode(res[0])
        m = head
        for i in range(1, len(res)):
            newnode = ListNode(res[i])
            m.next = newnode
            m = m.next
        return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next
