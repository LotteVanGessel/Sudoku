import pygame 
import sys
from const import WIDTH, HEIGHT, SQUARESIZE
from game import Game   
from square import Square 

class Main:
    def __init__(self) -> None:
            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Sudoku")
            self.motion_row = 0
            self.motion_col = 0
            self.keys = {pygame.K_1:1, pygame.K_2:2, pygame.K_3:3, pygame.K_4:4, pygame.K_5:5, pygame.K_6:6, pygame.K_7:7, pygame.K_8:8, pygame.K_9:9} 
            self.game = Game()

    def main_loop(self) -> None:
        while True:
            self.game.show_bg(surface = self.screen)
            self.game.show_hover(self.screen)
            self.game.show_numbers(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.motion_row = event.pos[1] // SQUARESIZE
                    self.motion_col = event.pos[0] // SQUARESIZE
                    self.game.set_hover(self.motion_row, self.motion_col)
                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    if key in self.keys:
                        if Square.in_range(self.motion_col, self.motion_row):
                            square = self.game.board.squares[self.motion_col][self.motion_row]
                            if  not square.static:
                                number = self.keys[key]
                                block = self.game.board.blocks[self.motion_col // 3][self.motion_row //3]
                                col = self.game.board.columns[self.motion_col]
                                row = self.game.board.rows[self.motion_col]
                                square.change_number(number)
                                block.remove_possible_number()
                                col.remove_possible_number()
                                row.remove_possible_number()
            pygame.display.update()

main = Main() 
main.main_loop()