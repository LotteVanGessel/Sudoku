from const import COLS, ROWS
from square import Square
from container import Row, Column, Block
import os
import copy

class Board:

    def __init__(self) -> None:
        self.squares = []
        self._create()
        self.rows = [Row() for _ in range(ROWS)]
        self.columns = [Column() for _ in range(COLS)]
        self.blocks = [Block() for _ in range(ROWS)]

    def _create(self):
        for row in range(ROWS):
            self.squares.append([])
            for col in range(COLS):
                self.squares[row].append(Square(row, col)) 
                