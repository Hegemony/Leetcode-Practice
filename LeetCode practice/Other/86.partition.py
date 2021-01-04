class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        dummpy1, dummpy2 = ListNode('~'), ListNode('!')
        p, q = dummpy1, dummpy2
        while head:
            if head.val < x:
                p.next = ListNode(head.val)
                p = p.next
            else:
                q.next = ListNode(head.val)
                q = q.next
            head = head.next
        p.next = dummpy2.next
        return dummpy1.next