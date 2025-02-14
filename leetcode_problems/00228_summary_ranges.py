# Problem Link: https://leetcode.com/problems/summary-ranges/
# Author: Dyanara Dela Rosa
# Date: Feb 13, 2024


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []

        start = nums[0]
        ranges = []
        for i in range(0, len(nums)):
            if i == len(nums)-1 or (i+1 < len(nums) and nums[i+1] != nums[i] + 1):
                if start == nums[i]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i]}")
                if i+1 < len(nums):
                    start = nums[i+1]

        return ranges
