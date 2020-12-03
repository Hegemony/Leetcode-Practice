# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        dummpy = ListNode(' ')
        dummpy.next = head
        p = dummpy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                break
            p = p.next
        return dummpy.next