class Square:
    
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col 
        self.number = None
        self.static = False
        self.possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.wrong = False

    def change_number(self, number):
        if self.number != number:
            if number not in self.possible_numbers:
                self.wrong = True
            self.number = number

    def __eq__(self, value: object) -> bool:
        return self.row == value.row and self.col == value.col 
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg >8:
                return False
        return True
    