import pygame

from const import ROWS, COLS, SQUARESIZE, HEIGHT, WIDTH
from board import Board
from square import Square

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.hovered_sqr = None
        self.big_font = pygame.font.SysFont('monospace', 24, bold = True)
        self.small_font = pygame.font.SysFont('monospace', 12, bold = True)
        self.possible_num_placement = {1:(0, 0), 2:(1,0), 3:(2,0), 4:(0,1), 5:(1,1), 6:(2,1), 7:(0,2), 8:(1,2),9:(2,2)}
        

    def show_bg(self, surface)->None:
        color_inside = "#ffffff"
        color_outside = "#000000"
        for row in range(ROWS):
            for col in range(COLS):
                rect = (col * SQUARESIZE, row *SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(surface, color_inside, rect)
                pygame.draw.rect(surface, color_outside, rect, width = 1)
        pygame.draw.line(surface,  "#000000", (0, 0 * SQUARESIZE), (HEIGHT, 0 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#000000", (0, 3 * SQUARESIZE), (HEIGHT, 3 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#000000", (0, 6 * SQUARESIZE), (HEIGHT, 6 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#000000", (0, 9 * SQUARESIZE), (HEIGHT, 9 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#000000", (0 * SQUARESIZE, 0 ), (0 * SQUARESIZE, WIDTH ), width = 4)
        pygame.draw.line(surface,  "#000000", (3 * SQUARESIZE, 0 ), (3 * SQUARESIZE, WIDTH ), width = 4)
        pygame.draw.line(surface,  "#000000", (6 * SQUARESIZE, 0 ), (6 * SQUARESIZE, WIDTH ), width = 4)
        pygame.draw.line(surface,  "#000000", (9 * SQUARESIZE, 0 ), (9* SQUARESIZE, WIDTH ), width = 4)
        
    def show_numbers(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                square =  self.board.squares[row][col]
                self.show_number(surface, square)

    def show_number(self, surface, square)->None:
        if square.number:
            row = square.row
            col = square.col
            font_color ="#6b6b6b"
            lbl = self.big_font.render(str(square.number), 1 , font_color)
            lbl_pos = (row* SQUARESIZE + SQUARESIZE / 4, col * SQUARESIZE + SQUARESIZE / 4)
            surface.blit(lbl, lbl_pos)
            if square.wrong:
                color = (244, 67, 54)
                rect = (row * SQUARESIZE, col * SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(surface, color, rect, width=3)

    def show_hover(self, surface):
        if self.hovered_sqr:
            color = (180, 180, 180)
            rect = (self.hovered_sqr.row * SQUARESIZE, self.hovered_sqr.col * SQUARESIZE, SQUARESIZE, SQUARESIZE)
            pygame.draw.rect(surface, color, rect, width=3)

    def set_hover(self, row, col):
        if Square.in_range(row, col):
            self.hovered_sqr = self.board.squares[row][col]


    def show_possible_numbers(self, surface):
        for row in self.board.squares:
            for square in row:
                if not square.number:
                    for pos_num in square.possible_numbers:
                        row = square.row
                        col = square.col
                        lbl = self.small_font.render(str(pos_num), 1 , "#6b6b6b")
                        x, y = self.possible_num_placement[pos_num]
                        lbl_pos = (row* SQUARESIZE + SQUARESIZE * x /3 + SQUARESIZE / 8, col * SQUARESIZE + SQUARESIZE * y /3 + SQUARESIZE / 8)
                        surface.blit(lbl, lbl_pos)



    def reset(self):
        self.__init__()