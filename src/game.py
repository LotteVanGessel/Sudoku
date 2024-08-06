import pygame

from const import ROWS, COLS, SQUARESIZE, HEIGHT, WIDTH
from board import Board
from square import Square

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.hovered_sqr = None
        self.font = pygame.font.SysFont('monospace', 24, bold = True)


    def show_bg(self, surface)->None:
        color_inside = "#ffffff"
        color_outside = "#000000"
        for row in range(ROWS):
            for col in range(COLS):
                rect = (col * SQUARESIZE, row *SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(surface, color_inside, rect)
                pygame.draw.rect(surface, color_outside, rect, width = 1)
        pygame.draw.line(surface,  "#000000", (0, 3 * SQUARESIZE), (HEIGHT, 3 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#000000", (0, 6 * SQUARESIZE), (HEIGHT, 6 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#000000", (0, 0 * SQUARESIZE), (HEIGHT, 0 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#000000", (0, 9 * SQUARESIZE), (HEIGHT, 9 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#000000", (3 * SQUARESIZE, 0 ), (3 * SQUARESIZE, WIDTH ), width = 4)
        pygame.draw.line(surface,  "#000000", (6 * SQUARESIZE, 0 ), (6 * SQUARESIZE, WIDTH ), width = 4)
        pygame.draw.line(surface,  "#000000", (9 * SQUARESIZE, 0 ), (9* SQUARESIZE, WIDTH ), width = 4)
        pygame.draw.line(surface,  "#000000", (0 * SQUARESIZE, 0 ), (0 * SQUARESIZE, WIDTH ), width = 4)

    
    def show_numbers(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                square =  self.board.squares[row][col]
                self.show_number(surface, square)

    def show_number(self, surface, square)->None:
        if square.number:
            color_font = "#6b6b6b"
            row = square.row
            col = square.col
            lbl = self.font.render(str(square.number), 1 , color_font)
            lbl_pos = (row* SQUARESIZE + SQUARESIZE / 4, col * SQUARESIZE + SQUARESIZE / 4)
            surface.blit(lbl, lbl_pos)

    def show_hover(self, surface):
        if self.hovered_sqr:
            color = (180, 180, 180)
            rect = (self.hovered_sqr.col * SQUARESIZE, self.hovered_sqr.row * SQUARESIZE, SQUARESIZE, SQUARESIZE)
            pygame.draw.rect(surface, color, rect, width=3)

    def set_hover(self, row, col):
        if Square.in_range(row, col):
            self.hovered_sqr = self.board.squares[row][col]


    def reset(self):
        self.__init__()