class Square:
    
    def __init__(self, row, col, piece=None) -> None:
        self.row = row
        self.col = col 
        self.number = None
        self.static = False
        self.possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __eq__(self, value: object) -> bool:
        return self.row == value.row and self.col == value.col 
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg >8:
                return False
        return True
    