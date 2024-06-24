# Problem link: https://leetcode.com/problems/merge-two-sorted-lists/
# Author: Dyanara Dela Rosa
# Date: June 15, 2024

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_ptr = list1
        list2_ptr = list2
        merged_list = None
        merged_list_ptr = None

        while list1_ptr or list2_ptr:
            if list2_ptr is None or (list1_ptr is not None and list1_ptr.val <= list2_ptr.val):
                new_node = ListNode(list1_ptr.val, None)
                list1_ptr = list1_ptr.next
            else:
                new_node = ListNode(list2_ptr.val, None)
                list2_ptr = list2_ptr.next

            if merged_list:
                merged_list_ptr.next = new_node
                merged_list_ptr = merged_list_ptr.next
            else:
                merged_list = new_node
                merged_list_ptr = merged_list
        return merged_list

