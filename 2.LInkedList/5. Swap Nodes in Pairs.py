from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 覆盖和maintain的内容 我需要很擅长解决这个问题 一个地方是初始化的问题 还有一个问题就是覆盖的问题，谨慎在linked list 中使用覆盖的问题
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        sign = False
        if not head or not head.next:
            return head
        while cur.next and cur.next.next or not sign:
            if sign:
                temp1 = cur.next
                temp2 = cur.next.next.next
                cur.next = cur.next.next
                cur.next.next = temp1
                temp1.next = temp2
                cur = cur.next.next

            else:
                sign = True
                temp1 = cur.next
                temp2 = temp1.next
                cur.next = cur.next.next
                temp1.next = cur
                head = temp1
                cur = head
                cur = cur.next
        return head

    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            temp1 = cur.next
            temp2 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = temp1
            temp1.next = temp2
            cur = cur.next.next
        return dummy.next

    # recursive
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        next = head.next.next
        cur.next = pre
        pre.next = self.swapPairs2(next)
        return cur


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
pre = solution.swapPairs(head)
while pre:
    print(pre.val)
    pre = pre.next
