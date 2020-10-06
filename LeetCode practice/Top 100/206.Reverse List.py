# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = head
        res = []
        while p != None:
            res.append(p.val)
            p = p.next

        if len(res) == 0:
            return None

        res.reverse()

        head1 = ListNode(res[0])
        q = head1
        for i in range(1, len(res)):
            q.next = ListNode(res[i])
            q = q.next
        return head1