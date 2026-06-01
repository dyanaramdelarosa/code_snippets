# Problem Link: https://leetcode.com/problems/add-digits/
# Author: Dyanara Dela Rosa
# Date: June 1, 2026


class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            new_num = 0
            for i in str(num):
                new_num += int(i)
            num = new_num
        return num