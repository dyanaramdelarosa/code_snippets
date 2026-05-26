# Problem Link: https://leetcode.com/problems/symmetric-tree/
# Author: Dyanara Dela Rosa
# Date: May 26, 2025


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_stack = [root.left]
        right_stack = [root.right]

        while True:
            if not left_stack and not right_stack:
                return True
            if not left_stack or not right_stack:
                return False

            left = left_stack.pop()
            right = right_stack.pop()

            if left is None and right is None:
                continue
            elif (
                not all([left, right])      # one item is None
                or left.val != right.val
            ):
                return False

            if left is not None:
                left_stack.append(left.left)
                left_stack.append(left.right)
            if right is not None:
                right_stack.append(right.right)
                right_stack.append(right.left)


