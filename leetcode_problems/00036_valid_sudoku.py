# Problem Link: https://leetcode.com/problems/valid-sudoku/
# Author: Dyanara Dela Rosa
# Date: Feb 19, 2025


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                num = board[i][j]
                grid_index = (i//3*3)+(j//3)
                if num == ".":
                    continue
                if num in row[i] or num in col[j] or num in grid[grid_index]: return False
                row[i].add(num)
                col[j].add(num)
                grid[grid_index].add(num)
        return True

