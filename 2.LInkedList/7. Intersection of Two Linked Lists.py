# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        dummy_a = ListNode(next=headA)
        dummy_b = ListNode(next=headB)
        cura = dummy_a
        curb = dummy_b
        lena, lenb = 0, 0
        while cura.next:
            lena += 1
            cura = cura.next
        while curb.next:
            lenb += 1
            curb = curb.next
        n = lena - lenb if lena > lenb else lenb - lena
        cura = dummy_a.next
        curb = dummy_b.next
        if lena > lenb:
            for _ in range(n):
                cura = cura.next
        elif lenb > lena:
            for _ in range(n):
                curb = curb.next
        while curb and cura:
            if cura == curb and cura and curb:
                return curb
            cura = cura.next
            curb = curb.next
        return None


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Helper function to find the node by index (used to create the intersection)
def get_node_by_index(head, index):
    current = head
    for _ in range(index):
        current = current.next
    return current


# Step 1: Create linked lists without intersection
listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1]

headA = create_linked_list(listA)
headB = create_linked_list(listB)

# Step 2: Create an intersection at the node with value `8` (index 2 in listA)
intersection_node = get_node_by_index(headA, 2)

# Step 3: Attach the intersection node to the end of listB
last_node_b = get_node_by_index(headB, 2)  # Last node in listB (node with value `1`)
last_node_b.next = intersection_node

# Now headA and headB are intersecting at the node with value `8`

# Test the function
solution = Solution()
intersection = solution.getIntersectionNode(headA, headB)
print(
    "Intersection Node Value:", intersection.val if intersection else "No intersection"
)
