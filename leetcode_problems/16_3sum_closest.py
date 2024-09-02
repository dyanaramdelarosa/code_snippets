# Problem Link: https://leetcode.com/problems/3sum-closest/
# Author: Dyanara Dela Rosa
# Date: September 2, 2024

class Solution:
    def get_total(self, nums):
        return sum(nums)

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        total = self.get_total(nums[:3])
        nums = sorted(nums)
        nums_len = len(nums)

        for i in range(0, nums_len):
            j = i+1
            k = nums_len-1

            while j<k:
                cur_total = self.get_total([nums[i], nums[j], nums[k]])
                if cur_total == target:
                    return cur_total
                if abs(cur_total - target) < abs(total - target):
                    total = cur_total
                if cur_total < target:
                    j += 1
                else:
                    k -=1
        i += 1
        return total
