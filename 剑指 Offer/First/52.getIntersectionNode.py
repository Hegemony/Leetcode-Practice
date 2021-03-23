# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA
        q = headB
        res = set()
        while p:
            res.add(p)
            p = p.next
        while q:
            if q not in res:
                res.add(q)
            else:
                return q
            q = q.next
        return None
