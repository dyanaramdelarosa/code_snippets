# Problem Link: https://leetcode.com/problems/zigzag-conversion
# Author: Dyanara Dela Rosa
# Date: June 28, 2024

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        str_groups = [""] * numRows
        index, direction = 0, 1

        for i in range(len(s)):
            str_groups[index] += s[i]
            index += direction
            if index == numRows - 1 or index == 0:
                direction *= -1

        return "".join(str_groups)

        # offset = numRows + (numRows - 2)
        # new_str = ""
        # i, j, k, swap = 0, 0, 0, 0
        # while i < len(s):
        #     if k < len(s):
        #         new_str += s[k]
        #         if j>0 and swap: 
        #             k += j*2
        #             swap = 0
        #         else: 
        #             k += offset
        #             if j>0 and not swap:
        #                 swap = 1
        #         i += 1

        #     else:
        #         j += 1
        #         k = j
        #         swap = 0
        #         if offset != 2: 
        #             offset = offset - 2
        #         else: 
        #             offset = numRows + (numRows - 2)
        # return new_str
