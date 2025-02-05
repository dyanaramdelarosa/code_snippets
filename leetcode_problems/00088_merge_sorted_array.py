# Problem Link: https://leetcode.com/problems/merge-sorted-array/
# Author: Dyanara Dela Rosa
# Date: Feb 5, 2025

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return

        insert_pos = len(nums1) - 1
        m = m-1
        n = n-1

        while n >= 0:
            if m < 0 or (nums1[m] < nums2[n]):
                nums1[insert_pos] = nums2[n]
                n -= 1
            else:
                nums1[insert_pos] = nums1[m]
                m -= 1
            insert_pos -= 1
