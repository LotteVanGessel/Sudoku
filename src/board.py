from const import COLS, ROWS
from square import Square
from container import Row, Column, Block
import os
import copy

class Board:

    def __init__(self) -> None:
        self.squares = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.columns = [Column() for _ in range(COLS)]
        self.rows = [Row() for _ in range(ROWS)]
        self.blocks = [[Block() for _ in range(3)] for _ in range(3)]
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