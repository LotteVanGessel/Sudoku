from const import COLS, ROWS
from square import Square
from container import Row, Column, Block
import os
import copy

class Board:

    def __init__(self) -> None:
        self.squares = []
        self.rows = [Row() for _ in range(ROWS)]
        self.columns = [Column() for _ in range(COLS)]
        self.blocks = [[Block() for _ in range(3)] for _ in range(3)]
        self._create()
        

    def _create(self):
        for row in range(ROWS):
            self.squares.append([])
            for col in range(COLS):
                new_square = Square(row, col)
                self.squares[row].append(new_square)
                self.rows[row].add_square(new_square) 
                self.columns[col].add_square(new_square) 
                self.blocks[row // 3][col // 3].add_square(new_square) 
                