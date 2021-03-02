class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        cur = dummpy = ListNode(' ')
        while p and q:
            if p.val < q.val:
                new = ListNode(p.val)
                cur.next = new
                cur = cur.next
                p = p.next
            else:
                new = ListNode(q.val)
                cur.next = new
                cur = cur.next
                q = q.next
        cur.next = p if p else q
        return dummpy.next
