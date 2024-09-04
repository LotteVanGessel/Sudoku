import z3
from const import ROWS, COLS

class SudokuSolver:
    def __init__(self) -> None:
        self.variables = [[ 0 for i in range(COLS)] for j in range(ROWS)]
        self.solution = [[ 0 for i in range(COLS)] for j in range(ROWS)]
        self.model = None 

    def parse_solution(self):
        if self.model:
            for var in self.model:
                _, row, col = str(var).split("_")
                self.solution[int(row)][int(col)] = int(self.model[var].as_string())
        print("done")

    def get_solution_number(self, row, col):
        return self.solution[row][col]  
    
    def solve(self, squares):
        if not self.model:
            s = z3.Solver()
            for row in range(ROWS):
                for col in range(COLS):
                    square = squares[row][col]
                    self.variables[row][col] = z3.Int(f"s_{row}_{col}")
                    x = self.variables[row][col]
                    if square.static:
                        s.add(x == square.number)
                    else:
                        s.add(z3.Or(x == 1, x == 2, x==3, x==4, x== 5, x==6, x==7, x==8, x ==9))
            for col in range(COLS):
                for i in range(1, 10):
                    s.add(z3.Or(self.variables[0][col] == i, self.variables[1][col] == i, self.variables[2][col] == i, self.variables[3][col] == i, self.variables[4][col] == i, self.variables[5][col] == i, self.variables[6][col] == i, self.variables[7][col] == i, self.variables[8][col] == i))
            for row in range(ROWS):
                for i in range(1, 10):
                    s.add(z3.Or(self.variables[row][0] == i, self.variables[row][1] == i, self.variables[row][2] == i, self.variables[row][3] == i, self.variables[row][4] == i, self.variables[row][5] == i, self.variables[row][6] == i, self.variables[row][7] == i, self.variables[row][8] == i))
            for j in range(3):
                for k in range(3):
                    for i in range(1, 10):
                        s.add(z3.Or(self.variables[j*3][k * 3] == i, self.variables[j*3 + 1][k*3] == i, self.variables[j*3 + 2][k*3] == i, self.variables[j*3][k*3+1] == i, self.variables[j*3 + 1][k*3 + 1] == i, self.variables[j*3 + 2][k*3 +1] == i, self.variables[j*3][k*3+2] == i, self.variables[j*3 + 1][k*3 + 2] == i, self.variables[j*3 + 2][k*3 +2] == i))
            s.check()
            m = s.model()
            self.model = m
            self.parse_solution()
            
