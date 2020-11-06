# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        p = head
        q = p.next
        while q:
            if q.val == val:
                p.next = q.next
            p = p.next
            q = q.next
        return head