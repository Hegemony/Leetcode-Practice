class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
        a = []  # 链表1
        b = []  # 链表2
        while(l1 != None):
            a.append(l1.val)
            l1 = l1.next
        while (l2 != None):
            b.append(l2.val)
            l2 = l2.next
        m = len(a)
        n = len(b)
        res = []
        for i in range(m):
                res.append(a[i])
        for j in range(n):
                res.append(b[j])

        res.sort()
        head = ListNode()  # 定义一个空链表表头
        l = head
        for i in range(len(res)):
            newnode = ListNode(res[i])
            l.next = newnode
            l = newnode  # 等价于l = l.next

        return head.next

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

print(mergeTwoLists(a1, a2))

"""
简洁写法
"""
def mergeTwoLists1(l1: ListNode, l2: ListNode):
    res = []
    while (l1 != None):
        res.append(l1.val)
        l1 = l1.next
    while (l2 != None):
        res.append(l2.val)
        l2 = l2.next
    res.sort()
    head = ListNode()
    l = head
    for i in range(len(res)):
        newnode = ListNode(res[i])
        l.next = newnode
        l = newnode  # 等价于l = l.next

    return head.next