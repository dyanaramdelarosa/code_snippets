# Problem Link: https://leetcode.com/problems/reverse-integer/
# Author: Dyanara Dela Rosa
# Date: August 1, 2024


class Solution:
    def reverse(self, x: int) -> int:
        limit = 2**31
        sign_flag = x < 0
        if sign_flag: x *= -1
        
        reversed_num = int(str(x)[::-1])
        if sign_flag:
            reversed_num *= -1
        
        if reversed_num < -1*limit or reversed_num >= limit -1:
            reversed_num = 0
        
        return reversed_num