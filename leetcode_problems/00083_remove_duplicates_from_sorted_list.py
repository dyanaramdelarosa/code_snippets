# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Author: Dyanara Dela Rosa
# Date: Feb 6, 2025


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        prev = dummy
        current = head

        while current:
            if prev.val == current.val:
                prev.next = current.next # delete the duplicate
                current = current.next
            else:
                current = current.next
                prev = prev.next
        return head
