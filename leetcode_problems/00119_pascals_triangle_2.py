# Problem Link: https://leetcode.com/problems/pascals-triangle-ii/
# Author: Dyanara Dela Rosa
# Date: Feb 10, 2025

import math

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # row = []

        # for i in range(0, rowIndex+1):
        #     row.append(math.comb(rowIndex, i))

        # row.append(math.comb(rowIndex, i)) for i in range(0, rowIndex+1)

        # return row

        # List comprehension
        # return [math.comb(rowIndex, i) for i in range(0, rowIndex+1)]

        # Compute half, flip other half
        row = [math.comb(rowIndex, i) for i in range(0, rowIndex//2+1)]
        row.extend(row[:(rowIndex+1)//2][::-1])

        return row