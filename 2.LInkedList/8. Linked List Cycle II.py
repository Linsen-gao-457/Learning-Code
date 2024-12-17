from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = dummy
        fast = dummy
        slow = slow.next
        if not fast.next:
            return None
        fast = fast.next.next
        index1 = 1
        while fast != slow and slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            index1 += 1
        if not fast or not slow:
            return None
        index2 = 1
        slow = slow.next
        fast = fast.next.next
        while fast != slow:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            index2 += 1
        index2 -= 1
        while index1 != 0:
            cur = fast
            new = dummy
            index1 -= 1
            for i in range(index1):
                new = new.next
            for i in range(index2):
                slow = slow.next
            if slow != new:
                return cur
            fast = new


def create_linked_list_with_cycle(values, pos):
    # 创建链表节点
    head = ListNode(values[0])
    current = head
    cycle_entry = None

    # 构建链表
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_entry = current  # 记录循环起点

    # 在指定位置创建循环
    if cycle_entry:
        current.next = cycle_entry

    return head


# 创建测试用例
values = [-1, -7, 7, -4, 19, 6, -9, -5, -2, -5]
pos = 6
head = create_linked_list_with_cycle(values, pos)
solution = Solution()
solution.detectCycle(head)
