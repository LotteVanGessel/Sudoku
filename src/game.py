import pygame

from const import ROWS, COLS, SQUARESIZE, S_HEIGHT, S_WIDTH, T_WIDTH
from board import Board
from square import Square
from button import Reset, Save, Solve
import threading

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.hovered_sqr = None
        self.big_font = pygame.font.SysFont('monospace', 24, bold = True)
        self.small_font = pygame.font.SysFont('monospace', 12, bold = True)
        self.possible_num_placement = {1:(0, 0), 2:(1,0), 3:(2,0), 4:(0,1), 5:(1,1), 6:(2,1), 7:(0,2), 8:(1,2),9:(2,2)}
        self.possible_numbers_position = {(0.0,0.0):1, (0.0,1.0):2, (0.0,2.0):3, (1.0,0.0):4, (1.0,1.0):5,(1.0,2.0):6,(2.0,0.0):7,(2.0,1.0):8, (2.0,2.0):9}
        self.pos_num_high_lighted = None
        self.offset = T_WIDTH - S_WIDTH
        self.buttons = [Solve(1, self.solve), Reset(2, self.reset), Save(3, self.save)] 
    
    def show_bg(self, surface):
        self.show_bg_sudoku(surface)
        self.show_bg_buttons(surface)

    def show_bg_sudoku(self, surface)->None:
        color_outside = "#1c0454"
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.squares[row][col]
                color_inside = "#6e79a6" if square.static else "#c2d2d9"
                rect = (self.offset + col * SQUARESIZE, row *SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(surface, color_inside, rect)
                pygame.draw.rect(surface, color_outside, rect, width = 1)
        pygame.draw.line(surface,  "#1c0454", (self.offset, 0 * SQUARESIZE), (self.offset + S_HEIGHT, 0 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#1c0454", (self.offset, 3 * SQUARESIZE), (self.offset + S_HEIGHT, 3 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#1c0454", (self.offset, 6 * SQUARESIZE), (self.offset + S_HEIGHT, 6 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#1c0454", (self.offset, 9 * SQUARESIZE), (self.offset + S_HEIGHT, 9 * SQUARESIZE), width = 4)
        pygame.draw.line(surface,  "#1c0454", (self.offset + 0 * SQUARESIZE, 0 ), (self.offset + 0 * SQUARESIZE, S_WIDTH ), width = 4)
        pygame.draw.line(surface,  "#1c0454", (self.offset + 3 * SQUARESIZE, 0 ), (self.offset  + 3 * SQUARESIZE, S_WIDTH ), width = 4)
        pygame.draw.line(surface,  "#1c0454", (self.offset + 6 * SQUARESIZE, 0 ), (self.offset + 6 * SQUARESIZE, S_WIDTH ), width = 4)
        pygame.draw.line(surface,  "#1c0454", (self.offset + 9 * SQUARESIZE, 0 ), (self.offset + 9* SQUARESIZE, S_WIDTH ), width = 4)
        
    def show_bg_buttons(self, surface) -> None:
        color_inside = "#c2d2d9"
        rect = (0, 0, self.offset, S_HEIGHT)
        pygame.draw.rect(surface, color_inside, rect)
        

    def show_numbers(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                square =  self.board.squares[row][col]
                self.show_number(surface, square)

    def show_number(self, surface, square)->None:
        if square.number:
            row = square.row
            col = square.col
            font_color = "#1c0454" if square.static else "#6e79a6"
            lbl = self.big_font.render(str(square.number), 1 , font_color)
            lbl_pos = (self.offset + col * SQUARESIZE + SQUARESIZE / 3, row * SQUARESIZE + SQUARESIZE / 4)
            surface.blit(lbl, lbl_pos)
            if square.wrong:
                color = (244, 67, 54)
                rect = (self.offset + col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(surface, color, rect, width=3)
            

    def show_hover(self, surface):
        if self.hovered_sqr:
            color = "#1c0454"
            rect = (self.offset + self.hovered_sqr.col * SQUARESIZE, self.hovered_sqr.row * SQUARESIZE, SQUARESIZE, SQUARESIZE)
            pygame.draw.rect(surface, color, rect, width=3)

    def set_hover(self, row, col):
        if Square.in_range(row, col):
            self.hovered_sqr = self.board.squares[row][col]
    
    def set_number_hover(self, row, col):
        if (row, col) in self.possible_numbers_position.keys():
            self.pos_num_high_lighted = self.possible_numbers_position[(row, col)]

    def show_possible_numbers(self, surface):
        for row in self.board.squares:
            for square in row:
                if not square.number:
                    for pos_num in square.possible_numbers:
                        if square.visible_possible_numbers[pos_num]:
                            color = "#735AB0" if (self.hovered_sqr and square == self.hovered_sqr and pos_num == self.pos_num_high_lighted) else "#1c0454"
                            row = square.row
                            col = square.col
                            lbl = self.small_font.render(str(pos_num), 1 , color)
                            x, y = self.possible_num_placement[pos_num]
                            lbl_pos = (self.offset + col* SQUARESIZE + SQUARESIZE * x /3 + SQUARESIZE / 8, row * SQUARESIZE + SQUARESIZE * y /3 + SQUARESIZE / 8)
                            surface.blit(lbl, lbl_pos)

    def show_buttons(self, surface):
        for button in self.buttons:
            self.show_button(surface, button)

    def show_button(self, surface, button):
        for (i, texture) in enumerate(button.textures):
            img = pygame.image.load(texture)
            img_center = tuple(map(sum, zip(button.position_first_letter, (button.width * i, 0 ))))
            texture_rect = img.get_rect(center = img_center)
            surface.blit(img, texture_rect)
        
    def save(self):
        pass
    
    def solve(self):
        thread = threading.Thread(target=self.board.solve)
        thread.start()
    
    def reset(self):
        self.__init__()