# Problem Link: https://leetcode.com/problems/add-two-numbers/
# Author: Dyanara Dela Rosa
# Date: June 24, 2024

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getNumber(self, l: [ListNode]):
        number = []
        node = l
        while node:
            number.append(str(node.val))
            node = node.next
        return int("".join(number)[::-1])

    def convertToListNode(self, nums: List[int]):
        root = ListNode(nums[0], None)
        node = root
        for i in range(1, len(nums)):
            node.next = ListNode(nums[i], None)
            node = node.next
        return root

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # firstNum = self.getNumber(l1)
        # secondNum = self.getNumber(l2)
        # return self.convertToListNode(list(str(firstNum + secondNum))[::-1])
        root, result = None, None
        l1_ptr, l2_ptr = l1, l2
        carry = 0

        while l1_ptr or l2_ptr:
            items_sum = carry
            if l1_ptr: items_sum = items_sum + l1_ptr.val
            if l2_ptr: items_sum = items_sum + l2_ptr.val

            carry = items_sum // 10
            pos_result = ListNode(items_sum % 10, None)

            if not result: root = result = pos_result
            else:
                result.next = pos_result
                result = result.next

            if l1_ptr: l1_ptr = l1_ptr.next
            if l2_ptr: l2_ptr = l2_ptr.next
        if carry:
            pos_result = ListNode(carry, None)
            result.next = pos_result

        return root




