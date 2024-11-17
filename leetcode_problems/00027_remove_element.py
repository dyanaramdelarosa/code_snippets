# Problem Link: https://leetcode.com/problems/remove-element/
# Author: Dyanara Dela Rosa
# Date: June 21, 2024

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i = 0
        # sep = len(nums)

        # while i!=sep:
        #     if nums[i] == val:
        #         nums[i], nums[sep-1] = nums[sep-1], nums[i]
        #         sep -= 1
        #     else:
        #         i += 1
        # return sep

        i, index = 0, 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
