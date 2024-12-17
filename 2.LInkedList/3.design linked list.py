# Old Code
class MyLinkedList1:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        cur = self.head
        while index > 0 and cur:
            cur = cur.next
            index -= 1
        return cur.val if cur else -1

    def addAtHead(self, val: int) -> None:
        dummy = ListNode(next=self.head)
        cur = dummy
        cur.next = ListNode(val=val, next=cur.next)
        self.head = dummy.next

    def addAtTail(self, val: int) -> None:
        cur = self.head
        new = ListNode(val=val)
        if not cur:
            cur = new
            self.head = cur
        else:
            while cur.next:
                cur = cur.next
            cur.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            while index > 1 and cur:
                cur = cur.next
                index -= 1
            if not cur:
                return
            new = ListNode(next=cur.next, val=val)
            cur.next = new

    def deleteAtIndex(self, index: int) -> None:
        dummy = ListNode(next=self.head, val=0)
        cur = dummy
        while index > 0 and cur.next:
            cur = cur.next
            index -= 1
        if cur.next:
            cur.next = cur.next.next
        self.head = dummy.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# New Code
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode()

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        cur = self.dummy_head.next
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val=val, next=self.dummy_head.next)
        self.dummy_head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        new = ListNode(val=val)
        while cur.next:
            cur = cur.next
        cur.next = new
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        cur.next = ListNode(val=val, next=cur.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        cur = self.dummy_head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
def test_my_linked_list():
    obj = MyLinkedList()
    obj.addAtHead(7)
    obj.addAtHead(2)
    obj.addAtHead(1)
    obj.addAtIndex(3, 0)
    obj.deleteAtIndex(2)
    obj.addAtHead(6)
    obj.addAtTail(4)
    result = obj.get(4)
    obj.addAtHead(4)
    obj.addAtIndex(5, 0)
    obj.addAtHead(6)


# Run the test case
test_my_linked_list()
