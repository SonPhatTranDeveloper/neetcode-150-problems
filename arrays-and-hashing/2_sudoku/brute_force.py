"""
A simple brute-force algorithm to check every row, column and 3x3 block
Author: Son Phat Tran
"""

from typing import List


class Solution:
    def __init__(self):
        self.cache = [0] * 9

    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        # Create cache
        self.create_cache()

        # Check the horizontal lines
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if self.is_in_cache(board[row][col]):
                        print("row", row)
                        return False
                    self.add_to_cache(board[row][col])
            self.clear_cache()

        # Check the vertical line
        for col in range(9):
            for row in range(9):
                if board[row][col] != ".":
                    if self.is_in_cache(board[row][col]):
                        print("col", col)
                        return False
                    self.add_to_cache(board[row][col])
            self.clear_cache()

        # Check the smaller squares
        positions = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]
        for row, col in positions:
            for r in range(3):
                for c in range(3):
                    if board[row + r][col + c] != ".":
                        if self.is_in_cache(board[row + r][col + c]):
                            print("block", row, col)
                            return False
                        self.add_to_cache(board[row + r][col + c])
            self.clear_cache()

        return True

    def create_cache(self):
        self.cache = [0] * 9

    def clear_cache(self):
        for i in range(9):
            self.cache[i] = 0

    def add_to_cache(self, item):
        index = ord(item) - ord("1")
        self.cache[index] = 1

    def is_in_cache(self, item):
        index = ord(item) - ord("1")
        return self.cache[index] != 0


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    sol = Solution()
    print(sol.is_valid_sudoku(board))

