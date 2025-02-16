# Problem Link: https://leetcode.com/problems/next-permutation/
# Author: Dyanara Dela Rosa
# Date: Feb 16, 2025


class Solution:
    def get_index_next_number(self, nums, current_idx):
        next_idx = current_idx+1
        for num in range(current_idx+1, len(nums)):
            if nums[num] > nums[current_idx] and nums[num] < nums[next_idx]:
                next_idx = num
        return next_idx

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                change = nums[i]
                next_number_index = self.get_index_next_number(nums, i)
                nums[i], nums[next_number_index] = nums[next_number_index], nums[i]
                nums[i+1: len(nums)] = sorted(nums[i+1: len(nums)])
                return
        nums.sort()
        return
