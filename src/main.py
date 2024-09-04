import pygame 
import sys
import threading


from const import  S_HEIGHT, SQUARESIZE, T_WIDTH
from game import Game   
from square import Square 


class Main:
    def __init__(self) -> None:
            pygame.init()
            self.screen = pygame.display.set_mode((T_WIDTH, S_HEIGHT))
            pygame.display.set_caption("Sudoku")
            self.motion_row = 0
            self.motion_col = 0
            self.pos_num = 1
            self.static = False
            self.keys = {pygame.K_1:1, pygame.K_2:2, pygame.K_3:3, pygame.K_4:4, pygame.K_5:5, pygame.K_6:6, pygame.K_7:7, pygame.K_8:8, pygame.K_9:9} 
            self.game = Game()
   

    def main_loop(self) -> None:
        board = self.game.board
        game = self.game
        while True:
            game.show_bg(surface = self.screen)
            game.show_hover(self.screen)
            game.show_numbers(self.screen)
            game.show_possible_numbers(self.screen)
            game.show_buttons(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    if event.pos[0] >= game.offset:
                        self.motion_row = (event.pos[1]) // SQUARESIZE
                        self.motion_col = (event.pos[0] - game.offset) // SQUARESIZE
                        self.pos_num_r = (event.pos[1]  - self.motion_row * SQUARESIZE) / SQUARESIZE * 3 // 1
                        self.pos_num_c = (event.pos[0] - game.offset - self.motion_col * SQUARESIZE) / SQUARESIZE * 3 // 1
                        game.set_hover(self.motion_row, self.motion_col)
                        game.set_number_hover(self.pos_num_r, self.pos_num_c)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] >= game.offset:
                        if game.pos_num_high_lighted and game.hovered_sqr:
                            game.hovered_sqr.visible_possible_numbers[game.pos_num_high_lighted] = not game.hovered_sqr.visible_possible_numbers[game.pos_num_high_lighted]
                    else:
                        for button in game.buttons:
                            if button.corners[0][0] <= event.pos[0] <= button.corners[0][1] and button.corners[1][0] <= event.pos[1] <= button.corners[1][1]:
                                button.press()
                                thread = threading.Thread(target=self.game.show_animation, args = (self.screen, button))
                                thread.start()
                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    if key in self.keys:
                        if Square.in_range(self.motion_col, self.motion_row):
                            square = board.squares[self.motion_row][self.motion_col]
                            number = self.keys[key]
                            square.change_number(number, self.static)
                            board.update_possible_numbers_square(self.motion_row, self.motion_col)
                    elif key == pygame.K_BACKSPACE:
                        if Square.in_range(self.motion_col, self.motion_row):
                            square = board.squares[self.motion_row][self.motion_col]
                            if square.number:
                                square.remove_number()
                                board.update_possible_numbers_square(self.motion_row, self.motion_col)
                    elif key == pygame.K_s:
                        self.static = False if self.static else True
                    elif key == pygame.K_e:
                        board.solve_whole_board(self.sol)
                    elif key == pygame.K_u:
                        if Square.in_range(self.motion_col, self.motion_row):
                            if board.sol.solution:
                                number = board.sol.get_solution_number(self.motion_row, self.motion_col)
                                square = board.squares[self.motion_row][self.motion_col]
                                square.change_number(number, self.static)
                                board.update_possible_numbers_square(self.motion_row, self.motion_col)
            pygame.display.update() 

main = Main() 
main.main_loop()