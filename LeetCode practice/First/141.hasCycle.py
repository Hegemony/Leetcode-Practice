class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        if not (fast and fast.next):
            return False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False