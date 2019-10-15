"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example:

  board =
  [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
  
  Given word = "ABCCED", return true.
  Given word = "SEE", return true.
  Given word = "ABCB", return false.

"""


class Solution:
    def exist(self, board, word):
        used_coords = set()
        word_idx = 0
        def mysearch(row, col):
            nonlocal word_idx
            # Assess whether the option is valid.
            if (0 <= row < len(board) and
                0 <= col < len(board[0]) and
                board[row][col] == word[word_idx] and
                (row, col) not in used_coords):
                # Try the option.
                word_idx += 1
                used_coords.add((row, col))
                # Maybe the goal has been reached
                if word_idx == len(word):
                    return True
                # Identify the following options.
                options = [(row, col+1), (row+1, col), (row, col-1), (row-1, col)]
                # Have other delegates assess each of the following options. If
                # any yields a successful outcome, then accept (decide on) the
                # current option.
                for opt_row, opt_col in options:
                    result = mysearch(opt_row, opt_col)
                    if result:
                        return True
                # If no options succeeds, backtrack on the current option and report
                # the inviability of the current option.
                word_idx -= 1
                used_coords.remove((row, col))
            # Report the inviaibility of the current option.
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                result = mysearch(row, col)
                if result:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    board = [['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']]
    cases = ["ABCCED", "SEE", "ABCB"]
    results = [solution.exist(board, case) for case in cases]
    print(results)
