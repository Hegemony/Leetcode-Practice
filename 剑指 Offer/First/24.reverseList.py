# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        dummpy = ListNode(' ')
        p = head
        q = None
        while p:
            tmp = p.next
            p.next = q
            p = p.next
            q = p
        return p