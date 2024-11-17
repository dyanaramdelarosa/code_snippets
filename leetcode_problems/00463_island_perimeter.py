# Problem Link: https://leetcode.com/problems/island-perimeter/
# Author: Dyanara Dela Rosa
# Date: June 6, 2024


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i-1 >= 0 and grid[i-1][j] == 1: perimeter -= 1
                    if i+1 < num_rows and grid[i+1][j] == 1: perimeter -= 1
                    if j-1 >= 0 and grid[i][j-1] == 1: perimeter -= 1
                    if j+1 < num_cols and grid[i][j+1] == 1: perimeter -= 1
        return perimeter