# Problem link: https://leetcode.com/problems/house-robber/
# Author: Dyanara Dela Rosa
# Date: June 19, 2024

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = []

        for i in range(0, len(nums)):
            rob.append(nums[i])
            if rob[:i-1]:
                rob[i] = rob[i] + max(rob[:i-1])
        return max(rob)
