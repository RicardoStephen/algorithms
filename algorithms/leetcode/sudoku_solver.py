"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
   sub-boxes of the grid.

Empty cells are indicated by the character '.'.

Example:

    Input:
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]

    Output:
    [["5","3","4","6","7","8","9","1","2"],
     ["6","7","2","1","9","5","3","4","8"],
     ["1","9","8","3","4","2","5","6","7"],
     ["8","5","9","7","6","1","4","2","3"],
     ["4","2","6","8","5","3","7","9","1"],
     ["7","1","3","9","2","4","8","5","6"],
     ["9","6","1","5","3","7","2","8","4"],
     ["2","8","7","4","1","9","6","3","5"],
     ["3","4","5","2","8","6","1","7","9"]]


https://leetcode.com/problems/sudoku-solver/
"""


class Solution:
    def solveSudoku(self, board):
        # Helpers
        def get_tile(row, col):
            return (row // 3)*3 + (col // 3)
        def next_tile(row, col):
            if col == 8:
                return row + 1, 0
            else:
                return row, col + 1
        # Options filters
        all_numbers = set(map(str, range(1, 10)))
        row_availables = [all_numbers.copy() for _ in range(9)]
        col_availables = [all_numbers.copy() for _ in range(9)]
        tile_availables = [all_numbers.copy() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                entry = board[row][col]
                if entry != '.':
                    row_availables[row].remove(entry)
                    col_availables[col].remove(entry)
                    tile_availables[get_tile(row, col)].remove(entry)
        # Search behavior
        def search(row, col):
            if board[row][col] != '.':
                if row == 8 and col == 8:
                    return True
                return search(*next_tile(row, col))
            options = (row_availables[row] &
                       col_availables[col] &
                       tile_availables[get_tile(row, col)])
            for option in options:
                # Set the option
                row_availables[row].remove(option)
                col_availables[col].remove(option)
                tile_availables[get_tile(row, col)].remove(option)
                # Test the option
                # Success
                if ((row == 8 and col == 8) or
                    search(*next_tile(row, col))):
                    board[row][col] = option
                    return True
                # Backtrack
                row_availables[row].add(option)
                col_availables[col].add(option)
                tile_availables[get_tile(row, col)].add(option)
            # Prune branch
            return False
        # Kickoff search
        search(0, 0)


if __name__ == '__main__':
    solution = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    solutions = [["5","3","4","6","7","8","9","1","2"],
                 ["6","7","2","1","9","5","3","4","8"],
                 ["1","9","8","3","4","2","5","6","7"],
                 ["8","5","9","7","6","1","4","2","3"],
                 ["4","2","6","8","5","3","7","9","1"],
                 ["7","1","3","9","2","4","8","5","6"],
                 ["9","6","1","5","3","7","2","8","4"],
                 ["2","8","7","4","1","9","6","3","5"],
                 ["3","4","5","2","8","6","1","7","9"]]
    solution.solveSudoku(board)
    print(board)
    assert(board == solutions)
