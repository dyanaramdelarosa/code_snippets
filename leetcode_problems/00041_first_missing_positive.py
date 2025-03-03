# Problem Link: https://leetcode.com/problems/first-missing-positive/
# Author: Dyanara Dela Rosa
# Date: Mar 3, 2025


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos_nums = set()
        maximum = 0
        for num in nums:
            if num > 0:
                if num > maximum:
                    maximum = num
                pos_nums.add(num)

        for num in range(1, maximum+1):
            if num not in pos_nums:
                return num
        return maximum+1