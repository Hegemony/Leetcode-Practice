# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    sum1 = 0
    sum2 = 0
    count = 0

    while(l1 != None):
        x = l1.val
        sum1 += x * 10**(count)
        count += 1
        l1 = l1.next

    count = 0
    while (l2 != None):
        x = l2.val
        sum2 += x * 10**(count)
        count += 1
        l2 = l2.next

    sum = sum1 + sum2

    d = sum % 10
    l3 = ListNode(d)   # 新建一个链表
    sum = sum // 10
    a = l3             # 用a链表去链接结点
    while (sum != 0):
        d = sum % 10
        newNode = ListNode(d)
        a.next = newNode
        a = newNode
        sum = sum // 10

    return l3

head = ListNode(1)
a1 = head
for i in range(2, 4):
    node = ListNode(i)
    a1.next = node
    a1 = a1.next

head2 = ListNode(5)
a2 = head2
for i in range(6, 8):
    node = ListNode(i)
    a2.next = node
    a2 = a2.next

print(addTwoNumbers(a1, a2))