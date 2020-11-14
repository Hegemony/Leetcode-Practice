# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        p = dummy
        q = head
        for i in range(n):
            q = q.next
        while q:
            p = p.next
            q = q.next
        p.next = p.next.next
        print(head.val, dummy)
        return dummy.next


print(Solution().removeNthFromEnd(ListNode(1), 1))