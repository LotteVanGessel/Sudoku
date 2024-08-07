class Container:
    def __init__(self) -> None:
        self.contained_squares = []
    
    def add_square(self, square):
        self.contained_squares.append(square)

    def remove_possible_number(self):
        all_in_number = [square.number for square in self.contained_squares]
        possible_numbers = [i for i in range(1, 10) if i not in all_in_number]
        for square in self.contained_squares:
            square.possible_numbers = possible_numbers
             
class Row(Container):
    def __init__(self) -> None:
        super().__init__()

class Block(Container):
    def __init__(self) -> None:
        super().__init__()

class Column(Container):
    def __init__(self) -> None:
        super().__init__()