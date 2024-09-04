import pygame
from const import S_HEIGHT, S_WIDTH, T_WIDTH

class Button:
    def __init__(self, func) -> None:
        self.textures = []
        self.width = 32
        self.height = 32
        self.position_first_letter = (0, 0)
        self.position = 0
        self.corners = [(0, 0), (0, 0)]
        self.func = func

    def press(self)-> None:
        self.func()

    def animate(self):
        for text in self.textures:
            pass

class Reset(Button):
    def __init__(self, pos, func) -> None:
        super().__init__(func)
        self.textures = ["./assets/keyboard_16.png", "./assets/keyboard_15.png", "./assets/keyboard_24.png", "./assets/keyboard_15.png", "./assets/keyboard_17.png"]
        self.position = pos
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]
    
    
class Save(Button):
    def __init__(self, pos, func) -> None:
        super().__init__(func)
        self.textures = ["./assets/keyboard_24.png", "./assets/keyboard_23.png", "./assets/keyboard_35.png", "./assets/keyboard_15.png"]
        self.position = pos
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]

class Solve(Button):
    def __init__(self, pos, func) -> None:
        super().__init__(func)
        self.textures = ["./assets/keyboard_24.png", "./assets/keyboard_10.png", "./assets/keyboard_31.png", "./assets/keyboard_35.png", "./assets/keyboard_15.png"]
        self.position = pos
        self.position_first_letter = ((T_WIDTH - S_WIDTH) / 2 - len(self.textures) * self.width / 2, S_HEIGHT / 4 + (self.position * self.height * 1.5))
        self.corners = [(self.position_first_letter[0] - self.width / 2, self.position_first_letter[0] - self.width / 2 + self.width * len(self.textures)), (self.position_first_letter[1] - self.height / 2, self.position_first_letter[1] + self.height / 2)]
