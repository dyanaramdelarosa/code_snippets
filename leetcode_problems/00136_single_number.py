# Problem Link: https://leetcode.com/problems/single-number/
# Author: Dyanara Dela Rosa
# Date: August 14, 2024


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate = 0
        for num in nums:
            no_duplicate = no_duplicate^num
        return no_duplicate
