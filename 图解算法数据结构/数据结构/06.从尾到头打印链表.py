# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode):
        p = head
        res = []
        while p:
            res.append(p.val)
            p = p.next
        res.reverse()
        return res