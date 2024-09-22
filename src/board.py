from const import COLS, ROWS
from square import Square
from container import Row, Column, Block
from solver import SudokuSolver
import os
import copy

class Board:

    def __init__(self) -> None:
        self.squares = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.columns = [Column() for _ in range(COLS)]
        self.rows = [Row() for _ in range(ROWS)]
        self.blocks = [[Block() for _ in range(3)] for _ in range(3)]
        self.sol = SudokuSolver()
        self.static = False
        self._create()
        
    def _create(self):
        for row in range(ROWS):
            self.squares.append([])
            for col in range(COLS):
                new_square = Square(row, col)
                self.squares[row][col] = new_square
                self.rows[row].add_square(new_square) 
                self.columns[col].add_square(new_square) 
                self.blocks[row // 3][col // 3].add_square(new_square) 
    
    def update_possible_numbers_square(self, row, col):
        rows = self.rows[row]
        cols = self.columns[col]
        block = self.blocks[row // 3][col // 3]
        for s in rows.contained_squares:
            s.set_possible_number(self)
        for s in cols.contained_squares:
            s.set_possible_number(self)
        for s in block.contained_squares:
            s.set_possible_number(self)
    
    def set_wrong(self, row, col):
        rows = self.rows[row]
        cols = self.columns[col]
        block = self.blocks[row // 3][col // 3]
        current_square = self.squares[row][col]
        number = current_square.number
        wrong = False
        for s in rows.contained_squares:
            if number == s.number and current_square != s:
                s.wrong = True
                wrong = True
        for s in cols.contained_squares:
            if number == s.number and current_square != s:
                s.wrong = True
                wrong = True
        for s in block.contained_squares:
            if number == s.number and current_square != s:
                s.wrong = True
                wrong = True
        current_square.wrong = wrong

    def remove_wrong(self, row, col, number):
        rows = self.rows[row]
        cols = self.columns[col]
        block = self.blocks[row // 3][col // 3]
        for s in rows.contained_squares:
            if number == s.number:
                self.set_wrong(s.row, s.col)
        for s in cols.contained_squares:
            if number == s.number:
                self.set_wrong(s.row, s.col)
        for s in block.contained_squares:
            if number == s.number:
                self.set_wrong(s.row, s.col)

    def change_number(self, row, col, number):
        square = self.squares[row][col]
        prev_number = square.number
        square.change_number(number, self.static)
        if prev_number:
            self.remove_wrong(row, col, prev_number)
        self.update_possible_numbers_square(row, col)
        self.set_wrong(row, col)

    def remove_number(self, row, col):
        square = self.squares[row][col]
        prev_number = square.number
        if square.number:
            square.remove_number()
            self.update_possible_numbers_square(row, col)
            self.remove_wrong(row,col, prev_number)

    def solve_whole_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.squares[row][col]
                number = self.sol.solution[row][col]
                square.change_number(number, False)
    
    def solve(self):
        self.sol.solve(self.squares)