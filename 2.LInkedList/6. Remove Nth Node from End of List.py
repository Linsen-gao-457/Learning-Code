# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        cur = dummy
        if not head:
            return head
        for n in range(n):
            cur = cur.next
        while cur:
            cur = cur.next
            if not cur:
                pre.next = pre.next.next
                return dummy.next
            pre = pre.next
