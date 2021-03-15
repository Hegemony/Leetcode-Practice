class Solution:
    def detectCycle(self , head ):
        # write code here
        slow, fast = head, head
        if not (fast and fast.next):
            return
        while fast and fast.next:
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