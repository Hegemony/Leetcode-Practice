# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
快慢指针官方写法
"""


class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


"""
快慢指针自己写法
"""


class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        if not (fast and fast.next):
            return

        while fast and fast.next:  # 判断是否有环
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


"""
哈希的方法
"""


class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        hash = {}
        p = head
        while p:
            if hash.get(p.next, -1) > 0:
                return p.next
            else:
                hash[p] = 1
            p = p.next
        return None
