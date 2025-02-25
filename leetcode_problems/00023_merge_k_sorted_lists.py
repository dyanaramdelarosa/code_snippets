# Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/
# Author: Dyanara Dela Rosa
# Date: Feb 26, 2025

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # build linked list as you go through each linked list
        # main = ListNode(0)

        # for i in range(len(lists)):
        #     insert_list_ptr = lists[i]
        #     main_ptr = main

        #     while insert_list_ptr:
        #         new_node = ListNode(insert_list_ptr.val)
        #         if not main_ptr.next:
        #             main_ptr.next = new_node
        #         elif main_ptr.next.val < insert_list_ptr.val:
        #             main_ptr = main_ptr.next
        #             continue
        #         elif main_ptr.next.val >= insert_list_ptr.val:
        #             new_node.next = main_ptr.next
        #             main_ptr.next = new_node
        #         insert_list_ptr = insert_list_ptr.next
        # return main.next

        # get all items first and sort it before building resulting linked list
        all_items = []
        for i in range(len(lists)):
            ptr = lists[i]
            while ptr:
                all_items.append(ptr.val)
                ptr = ptr.next

        all_items.sort()
        merged_list = ListNode(0)
        merged_list_ptr = merged_list
        for item in all_items:
            merged_list_ptr.next = ListNode(item)
            merged_list_ptr = merged_list_ptr.next

        return merged_list.next

