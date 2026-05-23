# Problem Link: https://leetcode.com/problems/reverse-bits/
# Author: Dyanara Dela Rosa
# Date: May 23, 2026


class Solution:
    # bit operations
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            bit = n&1
            n = n >> 1
            output= output << 1
            output = output | bit
        return output

    # naive implementation
    # def convertToBase2(self, n: int) -> str:
    #     bits = []
    #     for i in range(32, 0, -1):
    #         pos_value = 2 ** (i-1)
    #         if pos_value <= n:
    #             n -= pos_value
    #             bits.append("1")
    #         else:
    #             bits.append("0")
    #     return "".join(bits)

    # def convertToBase10(self, n: str) -> int:
    #     num = 0
    #     for idx, val in enumerate(n):
    #         num += (2 ** (32 - idx - 1) if val == "1" else 0)
    #     return num

    # def reverseBits(self, n: int) -> int:
    #     bits = self.convertToBase2(n)[::-1]
    #     return self.convertToBase10(bits)
