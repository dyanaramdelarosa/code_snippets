# Problem Link: https://leetcode.com/problems/path-sum/
# Author: Dyanara Dela Rosa
# Date: Mar 2, 2025


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        if root.left is None and root.right is None:
            return targetSum == root.val

        left_check, right_check = False, False
        if root.left:
            root.left.val = root.left.val + root.val
            left_check = self.hasPathSum(root.left, targetSum)
        if root.right:
            root.right.val = root.right.val + root.val
            right_check = self.hasPathSum(root.right, targetSum)
        return left_check or right_check
