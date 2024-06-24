# Problem Link: https://leetcode.com/problems/two-sum/
# Author: Dyanara Dela Rosa
# Date: June 14, 2024

from collections import Counter

class Solution:
    def linearSearch(self, nums, targets):
        indices = []
        for i in range(len(nums)):
            if targets[0] == nums[i] or targets[1] == nums[i]:
                indices.append(i)
            if len(indices) == 2:
                break
        return indices

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_counter = Counter(nums)
        for i in num_counter:
            if target-i in num_counter:
                if i == target-i and num_counter[i] == 1:
                    continue
                indices = self.linearSearch(nums, [i, target-i])
                return indices
