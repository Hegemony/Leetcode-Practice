# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        p = head
        res = []
        while p != None:
            res.append(p.val)
            p = p.next

        result = res.copy()
        result.reverse()  # 翻转列表

        return res == result

print(Solution().isPalindrome(ListNode(1)))

a = [1, 2]
b = a.copy()

print(a, b)
b.reverse()
print(a, b)