import pygame 
import sys
import threading


from const import  S_HEIGHT, SQUARESIZE, T_WIDTH
from button import Reset, Solve
from game import Game   
from square import Square 


class Main:
    def __init__(self) -> None:
            pygame.init()
            self.screen = pygame.display.set_mode((T_WIDTH, S_HEIGHT))
            pygame.display.set_caption("Sudoku")
            self.mouse_row = 0
            self.mouse_col = 0
            self.chosen_row = 0
            self.chosen_col = 0
            self.pos_num = 1
            self.keys = {pygame.K_1:1, pygame.K_2:2, pygame.K_3:3, pygame.K_4:4, pygame.K_5:5, pygame.K_6:6, pygame.K_7:7, pygame.K_8:8, pygame.K_9:9} 
            self.game = Game()
            self.game.set_chosen(self.chosen_row, self.chosen_col)
   

    def main_loop(self) -> None:
        while True:
            board = self.game.board
            game = self.game
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
                        self.mouse_row = (event.pos[1]) // SQUARESIZE
                        self.mouse_col = (event.pos[0] - game.offset) // SQUARESIZE
                        self.pos_num_r = (event.pos[1]  - self.mouse_row * SQUARESIZE) / SQUARESIZE * 3 // 1
                        self.pos_num_c = (event.pos[0] - game.offset - self.mouse_col * SQUARESIZE) / SQUARESIZE * 3 // 1
                        game.set_hover(self.mouse_row, self.mouse_col)
                        game.set_number_hover(self.pos_num_r, self.pos_num_c)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] >= game.offset:
                        if game.pos_num_high_lighted and game.hovered_sqr:
                            game.hovered_sqr.visible_possible_numbers[game.pos_num_high_lighted] = not game.hovered_sqr.visible_possible_numbers[game.pos_num_high_lighted]
                    else:
                        for button in game.buttons:
                            if button.corners[0][0] <= event.pos[0] <= button.corners[0][1] and button.corners[1][0] <= event.pos[1] <= button.corners[1][1]:
                                if isinstance(button, Reset):
                                    thread = threading.Thread(target=self.game.show_animation, args = (button,))
                                    thread.start()
                                    thread2 = threading.Thread(target=button.press)
                                    thread2.start()
                                elif isinstance(button, Solve):
                                    thread = threading.Thread(target=self.game.show_animation, args = (button, True))
                                    thread.start()
                                    thread2 = threading.Thread(target=button.press)
                                    thread2.start()
                                    thread3 = threading.Thread(target=self.game.stop_animating, args = (button, thread2.is_alive))
                                    thread3.start()
                                else:
                                    button.press()
                                    thread = threading.Thread(target=self.game.show_animation, args = (button,))
                                    thread.start()
                elif event.type == pygame.KEYDOWN:
                    key = event.key
                    if key in self.keys:
                        if Square.in_range(self.chosen_col, self.chosen_row):
                            square = board.squares[self.chosen_row][self.chosen_col]
                            number = self.keys[key]
                            square.change_number(number, board.static)
                            board.update_possible_numbers_square(self.chosen_row, self.chosen_col)
                    elif key == pygame.K_BACKSPACE:
                        if Square.in_range(self.mouse_col, self.mouse_row):
                            square = board.squares[self.chosen_row][self.chosen_col]
                            if square.number:
                                square.remove_number()
                                board.update_possible_numbers_square(self.chosen_row, self.chosen_col)
                    elif key == pygame.K_e:
                        board.solve_whole_board(self.sol)
                    elif key == pygame.K_u:
                        if Square.in_range(self.chosen_col, self.chosen_row):
                            if board.sol.solution:
                                number = board.sol.get_solution_number(self.chosen_row, self.chosen_col)
                                square = board.squares[self.chosen_row][self.chosen_col]
                                square.change_number(number, board.static)
                                board.update_possible_numbers_square(self.chosen_row, self.chosen_col)
                    elif key == pygame.K_UP or key == pygame.K_w:
                        self.chosen_row = self.chosen_row - 1 if Square.in_range(self.chosen_row - 1) else 8
                    elif key == pygame.K_DOWN or key == pygame.K_s:
                        self.chosen_row = self.chosen_row + 1 if Square.in_range(self.chosen_row + 1) else  0
                    elif key == pygame.K_RIGHT or key == pygame.K_d:
                        self.chosen_col = self.chosen_col + 1 if Square.in_range(self.chosen_col + 1) else 0
                    elif key == pygame.K_LEFT or key == pygame.K_a:
                        self.chosen_col = self.chosen_col - 1 if Square.in_range(self.chosen_col - 1) else 8
                    game.set_chosen(self.chosen_row, self.chosen_col)
            pygame.display.update() 

main = Main() 
main.main_loop()