# Problem Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Author: Dyanara Dela Rosa
# Date: Feb 7, 2025


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        node = TreeNode(nums[mid], None, None)

        if len(nums) == 1: return node
        if start <= mid - 1:
            node.left = self.sortedArrayToBST(nums[:mid])
        if mid + 1 <= end:
            node.right = self.sortedArrayToBST(nums[mid+1:])

        return node
