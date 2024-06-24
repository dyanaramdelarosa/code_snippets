# Problem Link: https://leetcode.com/problems/plus-one/
# Author: Dyanara Dela Rosa
# Date: June 23, 2024

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits) - 1:
                value = digits[i] + 1
            else:
                value = digits[i] + carry
            digits[i] = value % 10
            carry = value // 10
            if carry == 0:
                return digits
        if carry != 0:
            digits.insert(0, carry)
        return digits


        # value = int("".join(str(x) for x in digits))
        # value += 1
        # return list(int(x) for x in str(value))


