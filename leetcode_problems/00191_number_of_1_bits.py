# Problem Link: https://leetcode.com/problems/number-of-1-bits/
# Author: Dyanara Dela Rosa
# Date: May 24, 2026


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n&1
            n = n >> 1
        return count
