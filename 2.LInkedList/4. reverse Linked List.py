# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # my solution is not good, cause i use two pointers to adjust the value in hte output
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            if cur == head:
                new = ListNode(val=cur.val)
            else:
                new = ListNode(val=cur.val, next=old.nex)
                old.next = new
            cur = cur.next

        return new

    #   双指针
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre

    # 递归
    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)

    def reverse(self, cur: ListNode, pre: ListNode):
        if not cur:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
pre = solution.reverseList3(head)
print("begin")
while pre:
    print(pre.val)
    pre = pre.next
