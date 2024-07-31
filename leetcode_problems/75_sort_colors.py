# Problem Link: https://leetcode.com/problems/sort-colors/
# Author: Dyanara Dela Rosa
# Date: June 6, 2024

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) == 1: return

        first = -1
        second = -1
        third = len(nums)
        i = 0
        while True:
            i = second + 1

            if nums[i] == 0:
                nums[i], nums[first+1] = nums[first+1], nums[i]
                first += 1
                second += 1
            elif nums[i] == 1:
                second += 1
            elif nums[i] == 2:
                nums[i], nums[third - 1] = nums[third - 1], nums[i]
                third -= 1
            if second + 1 == third:
                break