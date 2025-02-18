# Problem Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Author: Dyanara Dela Rosa
# Date: Feb 18, 2024


class Solution:
    def binary_search(self, nums: List[int], target:int, left: int, right: int):
        if left > right: return [-1, -1]

        mid = (left + right) // 2
        if nums[mid] < target:
            return self.binary_search(nums, target, mid+1, right)
        elif nums[mid] > target:
            return self.binary_search(nums, target, left, mid-1)
        else:
            start, end = mid, mid
            # find start and end position
            while start >= 0 and nums[start] == target:
                start -= 1

            while end < len(nums) and nums[end] == target:
                end += 1

            return [start+1, end-1]


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binary_search(nums, target, 0, len(nums)-1)