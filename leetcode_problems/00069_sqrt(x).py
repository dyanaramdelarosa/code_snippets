# Problem Link: https://leetcode.com/problems/sqrtx/
# Author: Dyanara Dela Rosa
# Date: June 21, 2024

class Solution:
    def mySqrt(self, x: int) -> int:
        # i = 0
        # while i*i <= x:
        #     i += 1
        # return i - 1

        left = 1
        right = x

        while left <= right:
            mid = (left + right)//2
            mid_squared = mid * mid
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
