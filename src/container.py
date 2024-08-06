class Container:
    def __init__(self) -> None:
        self.contained_squares = []

class Row(Container):
    def __init__(self) -> None:
        super.__init__()

class Block(Container):
    def __init__(self) -> None:
        super.__init__()

class Column(Container):
    def __init__(self) -> None:
        super.__init__()