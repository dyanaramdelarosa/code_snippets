# Problem Link: https://leetcode.com/problems/search-insert-position/
# Author: Dyanara Dela Rosa
# Date: June 23, 2024

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return right
