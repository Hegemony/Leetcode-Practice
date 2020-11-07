# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        head = ListNode(0)
        l = head
        while p and q:
            if p.val <= q.val:
                newnode = ListNode(p.val)
                l.next = newnode
                l = l.next
                p = p.next
            else:
                newnode = ListNode(q.val)
                l.next = newnode
                l = l.next
                q = q.next
        l.next = p if p else q
        return head.next

