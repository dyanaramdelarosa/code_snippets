# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p2 = p1 = head
        while p1 is not None:
            if p1.val == val:
                if head == p1 == p2:
                    head = p1 = p2 = head.next
                else:
                    p1 = p1.next
                    p2.next = p1
            else:
                p1 = p1.next
                if p2.next != p1:
                    p2 = p2.next
        return head
