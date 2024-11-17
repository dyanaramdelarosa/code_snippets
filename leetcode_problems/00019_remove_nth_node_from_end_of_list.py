# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Author: Dyanara Dela Rosa
# Date: November 10, 2024

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        left_ptr = right_ptr = head
        count = 1

        while right_ptr.next:
            right_ptr = right_ptr.next
            count += 1
        
        pos = count - n
        if pos == 0:
            return head.next

        for i in range(pos-1):
            left_ptr = left_ptr.next
        left_ptr.next = left_ptr.next.next

        return head
