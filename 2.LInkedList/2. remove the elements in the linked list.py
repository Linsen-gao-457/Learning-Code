from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next


def creat_from_list2linked(list):
    dummy = ListNode()
    cur = dummy
    for i in list:
        cur.next = ListNode(val=i)
        cur = cur.next
    return dummy.next


def ListNode2List(head):
    cur = head
    list = []
    while cur:
        list.append(cur.val)
        cur = cur.next
    return list


def main():
    list = [6, 1, 2, 3, 4, 6, 5]
    val = 6

    head = creat_from_list2linked(list)
    solution = Solution()
    output1 = solution.removeElements1(head, val)
    List = ListNode2List(output1)
    print(List)
    output2 = solution.removeElements2(head, val)
    List = ListNode2List(output2)
    print(List)


if __name__ == "__main__":
    main()
