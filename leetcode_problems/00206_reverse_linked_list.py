# Problem Link: https://leetcode.com/problems/reverse-linked-list/
# Author: Dyanara Dela Rosa
# Date: May 29, 2025

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = nxt = None
        if head.next:
            nxt = head.next

        while True:
            head.next = prev
            if nxt is None:
                break
            prev = head
            head = nxt
            nxt = nxt.next
        return head
