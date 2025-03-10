# Problem Link: https://leetcode.com/problems/linked-list-cycle/
# Author: Dyanara Dela Rosa
# Date: Mar 10, 2025

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr, fast_ptr = head, None
        if slow_ptr:
            fast_ptr = slow_ptr.next
        while fast_ptr and slow_ptr:
            if fast_ptr == slow_ptr:
                return True
            slow_ptr = slow_ptr.next
            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next
            else: break
        return False
