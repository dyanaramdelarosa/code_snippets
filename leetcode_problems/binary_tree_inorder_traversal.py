# Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Author: Dyanara Dela Rosa
# Date: June 17, 2024

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        stack = []
        visited = []

        # while True:
        #     if node and node.val not in visited:
        #         stack.append(node)
        #         node = node.left
        #         continue
        #     else:
        #         if not stack: return visited
        #         node = stack.pop()
        #         if node not in visited:
        #             visited.append(node.val)
        #             if node.right:
        #                 node=node.right

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            visited.append(root.val)
            root = root.right
        return visited
            