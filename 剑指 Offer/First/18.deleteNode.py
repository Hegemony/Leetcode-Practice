# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummpy = ListNode(' ')
        p = head
        dummpy.next = head
        while p:
            if p.val == val:
                p.next.next = p.next
                break
            p = p.next
        return dummpy.next