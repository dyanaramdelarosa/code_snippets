# Problem Link: https://leetcode.com/problems/3sum-closest/
# Author: Dyanara Dela Rosa
# Date: September 2, 2024

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        total = float('inf')
        nums.sort()
        nums_len = len(nums)

        for i in range(0, nums_len):
            left = i + 1
            right = nums_len - 1

            while left < right:
                cur_total = nums[i] + nums[left] + nums[right]
                if cur_total == target:
                    return cur_total
                if abs(cur_total - target) < abs(total - target):
                    total = cur_total
                if cur_total < target:
                    left += 1
                else:
                    right -= 1
        return total
