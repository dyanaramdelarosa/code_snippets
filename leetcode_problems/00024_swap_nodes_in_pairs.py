# Problem Link: https://leetcode.com/problems/swap-nodes-in-pairs/
# Author: Dyanara Dela Rosa
# Date: Mar 27, 2025


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = head.next
        head = right

        while left is not None:
            left.next = right.next
            right.next = left
            if left.next and left.next.next:
                prev = left
                right = left.next.next
                left = left.next
                prev.next = right
            else:
                break

        return head
