class Square:
    
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col 
        self.number = None
        self.static = False
        self.possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.wrong = False

    def change_number(self, number, static):
        if static:
            self.static = True
            self.number = number
        elif not self.static:
            self.number = number
            if number not in self.possible_numbers:
                self.wrong = True
        

    def remove_number(self):
        self.wrong = False
        self.static = False
        self.number = None

    def set_possible_number(self, board):
        row = board.rows[self.row]
        col = board.columns[self.col]
        block = board.blocks[self.row // 3][self.col// 3]
        numbers = row.get_all_numbers() + col.get_all_numbers() + block.get_all_numbers()
        self.possible_numbers = [i for i in self.all_numbers if i not in numbers]
        
    def __eq__(self, value: object) -> bool:
        return self.row == value.row and self.col == value.col 
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg >8:
                return False
        return True
    