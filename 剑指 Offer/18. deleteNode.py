# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if head.val == val:    # 头节点
            head = head.next
        p = head
        while p.next != None:   # 中间节点
            if p.next.val == val:
                p.next = p.next.next
                break   # 符合语句结束while
            p = p.next
        return head


"""
题解：双指针写法
"""

class Solution1:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head
