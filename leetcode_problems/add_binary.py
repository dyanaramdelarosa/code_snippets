# Problem Link: https://leetcode.com/problems/add-binary/
# Author: Dyanara Dela Rosa
# Date: July 20, 2024


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return str(bin(int(a,2)+int(b,2)))[2:]

        a_itr = len(a) - 1
        b_itr = len(b) - 1
        carry = 0
        result = ""

        while a_itr >= 0 or b_itr >= 0:
            if a_itr >= 0:
                carry += int(a[a_itr])
            if b_itr >= 0:
                carry += int(b[b_itr])
            a_itr -= 1
            b_itr -= 1

            result += str(carry % 2)
            carry = carry // 2

        if carry:
            result += str(carry)
        return result[::-1]
