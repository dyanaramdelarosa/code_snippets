# Problem Link: https://leetcode.com/problems/single-number/
# Author: Dyanara Dela Rosa
# Date: Feb 12, 2024

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_counter = set()

        for num in nums:
            if num in nums_counter:
                return True
            nums_counter.add(num)
        return False