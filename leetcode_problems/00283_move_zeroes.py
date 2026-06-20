# Problem Link: https://leetcode.com/problems/move-zeroes/
# Author: Dyanara Dela Rosa
# Date: June 20, 2026


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        0 1 0 2 3 4 5
        1 0 0 2 3 4 5
        1 2 0 0 3 4 5
        1 2 3 0 0 4 5
        1 2 3 4 0 0 5
        1 2 3 4 5 0 0
        """
        # zero_pos = -1
        # idx = 0
        # while idx < len(nums):
        #     if nums[idx] == 0:          # found a zero
        #         if zero_pos == -1:      # no zero yet
        #             zero_pos = idx      # assign zero value
        #     else:                       # not a zero
        #         if zero_pos != -1:
        #             nums[zero_pos], nums[idx] = nums[idx], nums[zero_pos]
        #             zero_pos += 1
        #     idx += 1

        non_zero_ptr = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_ptr], nums[i] = nums[i], nums[non_zero_ptr]
                non_zero_ptr += 1