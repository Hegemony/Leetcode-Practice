# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummpy = ListNode(0)
        dummpy.next = head
        p = dummpy
        q = head
        for i in range(n):
            q = q.next
        while q:
            q = q.next
            p = p.next
        p.next = p.next.next
        return dummpy.next