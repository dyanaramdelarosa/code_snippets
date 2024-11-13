# Problem Link: https://leetcode.com/problems/majority-element/
# Author: Dyanara Dela Rosa
# Date: November 12, 2024

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using built-in python
        return Counter(nums).most_common()[0][0]

        # using hashmap
        # most_common_item = occurrence = 0
        # histogram = {}

        # for num in nums:
        #     histogram[num] = 1 + histogram.get(num, 0)
        #     if histogram[num] > occurrence:
        #         most_common_item = num
        #         occurrence = histogram[num]
        # return most_common_item
        
        # using a majority 
