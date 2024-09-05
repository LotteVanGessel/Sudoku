import pygame
import time
from const import S_HEIGHT, S_WIDTH, T_WIDTH

class Button:
    def __init__(self, pos ,func) -> None:
        self.textures = []
        self.pressed_textures = []
        self.width = 32
        self.height = 32
        self.position_first_letter = (0, 0)
        self.position = pos
        self.corners = [(0, 0), (0, 0)]
        self.func = func
        self.sound_path = "./assets/sounds/key_board_click.wav"
        self.sound = pygame.mixer.Sound(self.sound_path)
        self.animating = False


    def press(self)-> None:
        self.func()


class Reset(Button):
    def __init__(self, pos ,func) -> None:
        super().__init__(pos ,func)
        self.textures = ["./assets/images/keyboard_16.png", "./assets/images/keyboard_15.png", "./assets/images/keyboard_24.png", "./assets/images/keyboard_15.png", "./assets/images/keyboard_17.png"]
        self.pressed_textures = ["./assets/images/keyboard_117.png", "./assets/images/keyboard_116.png", "./assets/images/keyboard_125.png", "./assets/images/keyboard_116.png", "./assets/images/keyboard_118.png"]
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]
        

    def press(self) -> None:
        while self.animating:
            time.sleep(0.01)
        self.func()
    
class Save(Button):
    def __init__(self, pos, func) -> None:
        super().__init__(pos ,func)
        self.textures = ["./assets/images/keyboard_24.png", "./assets/images/keyboard_23.png", "./assets/images/keyboard_35.png", "./assets/images/keyboard_15.png"]
        self.pressed_textures = ["./assets/images/keyboard_125.png", "./assets/images/keyboard_124.png", "./assets/images/keyboard_136.png", "./assets/images/keyboard_116.png"]
        self.position = pos
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]

class Load(Button):
    def __init__(self, pos ,func) -> None:
        super().__init__(pos ,func)
        self.textures = ["./assets/images/keyboard_31.png", "./assets/images/keyboard_21.png", "./assets/images/keyboard_23.png", "./assets/images/keyboard_25.png"]
        self.pressed_textures = ["./assets/images/keyboard_132.png", "./assets/images/keyboard_122.png", "./assets/images/keyboard_124.png", "./assets/images/keyboard_126.png"]
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]
 

class Solve(Button):
    def __init__(self, pos, func) -> None:
        super().__init__(pos ,func)
        self.textures = ["./assets/images/keyboard_24.png", "./assets/images/keyboard_10.png", "./assets/images/keyboard_31.png", "./assets/images/keyboard_35.png", "./assets/images/keyboard_15.png"]
        self.pressed_textures = ["./assets/images/keyboard_125.png", "./assets/images/keyboard_111.png", "./assets/images/keyboard_132.png", "./assets/images/keyboard_136.png", "./assets/images/keyboard_116.png"]
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]

class Show_board(Button):
    def __init__(self, pos ,func) -> None:
        super().__init__(pos, func)
        self.textures = ["./assets/images/keyboard_24.png", "./assets/images/keyboard_28.png", "./assets/images/keyboard_21.png", "./assets/images/keyboard_14.png", "", "./assets/images/keyboard_36.png", "./assets/images/keyboard_21.png", "./assets/images/keyboard_23.png", "./assets/images/keyboard_16.png", "./assets/images/keyboard_25.png"]
        self.pressed_textures = ["./assets/images/keyboard_125.png", "./assets/images/keyboard_129.png", "./assets/images/keyboard_122.png", "./assets/images/keyboard_115.png", "", "./assets/images/keyboard_137.png", "./assets/images/keyboard_122.png", "./assets/images/keyboard_124.png", "./assets/images/keyboard_117.png", "./assets/images/keyboard_126.png"]
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]


class Show_cell(Button):
    def __init__(self, pos ,func) -> None:
        super().__init__(pos, func)
        self.textures = ["./assets/images/keyboard_24.png", "./assets/images/keyboard_28.png", "./assets/images/keyboard_21.png", "./assets/images/keyboard_14.png", "", "./assets/images/keyboard_34.png", "./assets/images/keyboard_15.png", "./assets/images/keyboard_31.png", "./assets/images/keyboard_31.png"]
        self.pressed_textures = ["./assets/images/keyboard_125.png", "./assets/images/keyboard_129.png", "./assets/images/keyboard_122.png", "./assets/images/keyboard_115.png", "", "./assets/images/keyboard_135.png", "./assets/images/keyboard_116.png", "./assets/images/keyboard_132.png", "./assets/images/keyboard_132.png"]
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]

class Show_clues(Button):
     def __init__(self, pos ,func) -> None:
        super().__init__(pos, func)
        self.textures = ["./assets/images/keyboard_24.png", "./assets/images/keyboard_28.png", "./assets/images/keyboard_21.png", "./assets/images/keyboard_14.png", "", "./assets/images/keyboard_34.png", "./assets/images/keyboard_31.png", "./assets/images/keyboard_19.png", "./assets/images/keyboard_15.png"]
        self.pressed_textures = ["./assets/images/keyboard_125.png", "./assets/images/keyboard_129.png", "./assets/images/keyboard_122.png", "./assets/images/keyboard_115.png", "", "./assets/images/keyboard_135.png", "./assets/images/keyboard_132.png", "./assets/images/keyboard_120.png", "./assets/images/keyboard_116.png"]
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]
