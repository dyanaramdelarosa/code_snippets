# Problem Link: https://leetcode.com/problems/pascals-triangle/
# Author: Dyanara Dela Rosa
# Date: Feb 9, 2025

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        for row in range(1, numRows+1):
            pascal_row = []
            for col in range(row):
                if col == 0 or col == row - 1:
                    pascal_row.append(1)
                else:
                    pascal_row.append(pascal_triangle[row-2][col-1] + pascal_triangle[row-2][col])
            pascal_triangle.append(pascal_row)
        return pascal_triangle
