# Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Author: Dyanara Dela Rosa
# Date: June 16, 2024

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for i in range(len(nums) - 2, -1, -1):
        #     if nums[i] == nums[i+1]:
        #         nums.pop(i+1)
        # return len(nums)

        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cur]:
                nums[cur+1] = nums[i]
                cur += 1
        return cur+1
