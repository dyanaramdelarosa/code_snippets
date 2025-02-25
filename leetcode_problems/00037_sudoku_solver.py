# Problem Link: https://leetcode.com/problems/sudoku-solver/
# Author: Dyanara Dela Rosa
# Date: Feb 25, 2025


class Solution:
    def init_alt_storage(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                grid_index = i // 3 * 3 + j // 3
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grid[grid_index].add(board[i][j])

        return {"rows": rows, "cols": cols, "grids": grid}

    def add_item_in_alt_storage(self, alt_board, row, col, value):
        grid_index = row // 3 * 3 + col // 3
        alt_board["rows"][row].add(value)
        alt_board["cols"][col].add(value)
        alt_board["grids"][grid_index].add(value)

    def remove_item_in_alt_storage(self, alt_board, row, col, value):
        grid_index = row // 3 * 3 + col // 3
        alt_board["rows"][row].remove(value)
        alt_board["cols"][col].remove(value)
        alt_board["grids"][grid_index].remove(value)

    def is_valid_cell_value(self, alt_board, row, col, value) -> bool:
        if value in alt_board["rows"][row]:
            return False
        if value in alt_board["cols"][col]:
            return False
        grid_index = row // 3 * 3 + col // 3
        if value in alt_board["grids"][grid_index]:
            return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = [[[] for _ in range(9)] for _ in range(9)]
        alt_board = self.init_alt_storage(board)

        row, col = 0, 0

        while row < 9:
            while col < 9:
                if board[row][col] == ".":
                    if not stack[row][col]:
                        stack[row][col] = [
                            str(i)
                            for i in range(1, 10)
                            if self.is_valid_cell_value(alt_board, row, col, str(i))
                        ]
                        if stack[row][col]:
                            board[row][col] = stack[row][col][-1]
                            self.add_item_in_alt_storage(
                                alt_board, row, col, board[row][col]
                            )

                    while not stack[row][col]:
                        if col == 0:
                            row -= 1
                            col = 8
                        else:
                            col -= 1
                        if stack[row][col]:
                            popped_item = stack[row][col].pop()
                            self.remove_item_in_alt_storage(
                                alt_board, row, col, popped_item
                            )
                            if not stack[row][col]:
                                board[row][col] = "."
                                continue
                            else:
                                board[row][col] = stack[row][col][-1]
                                self.add_item_in_alt_storage(
                                    alt_board, row, col, board[row][col]
                                )

                col += 1
            row += 1
            col = 0

        return board
