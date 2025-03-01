# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Author: Dyanara Dela Rosa
# Date: Mar 1, 2025

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # left_height, right_height = 0, 0
        # if root is None:
        #     return 0
        # if root.left is None and root.right is None:
        #     return 1
        #
        # if root.left:
        #     left_height = 1+self.maxDepth(root.left)
        # if root.right:
        #     right_height = 1+self.maxDepth(root.right)
        #
        # if left_height >= right_height:
        #     return left_height
        # return right_height

        if root is None:
            return 0
        left_height = 1+self.maxDepth(root.left)
        right_height = 1+self.maxDepth(root.right)
        return max(left_height, right_height)
