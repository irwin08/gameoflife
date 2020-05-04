import cell

class Board:

    def __init__(self, n, m):
        self.generateBoard(n,m)

    def generateBoard(self, n, m):
        self.board = []
        for i in range(0,n):
            self.board.append([])
            for j in range(0,m):
                self.board[i].append(cell.Cell(i,j)) #add empty cell
                
