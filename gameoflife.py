import board
import copy

class GameOfLife:
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.board = board.Board(n,m)
        self.turn = 0

    def print_board(self):
        for i in range(0,self.n):
            for j in range(0,self.m):
                print(self.board.board[i][j].state, end='')
            print("")

    def set_board(self, board_list):
        self.board.board = board_list
        
            
    def advance(self):
        self.turn += 1

        new_board = copy.deepcopy(self.board)

        for i in range(0,self.n):
            for j in range(0,self.m):
                if self.get_neighbors(self.board.board[i][j]) < 2:
                    new_board.board[i][j].change_state(0)
                    
                elif self.get_neighbors(self.board.board[i][j]) > 3:
                    new_board.board[i][j].change_state(0)
               
                elif self.board.board[i][j].state == 0 and self.get_neighbors(self.board.board[i][j]) == 3:
                    new_board.board[i][j].change_state(1)

        self.board = new_board
                

    def get_neighbors(self, cell):
        num_of_neighbors = 0

        if cell.x == 0 and cell.y == 0:
            if self.board.board[cell.x+1][cell.y].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y+1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x][cell.y+1].state == 1:
                num_of_neighbors += 1
                
        elif cell.x == 0 and cell.y != 0 and cell.y != self.m-1:
            if self.board.board[cell.x][cell.y-1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y-1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y+1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x][cell.y+1].state == 1:
                num_of_neighbors += 1
                
        elif cell.x == 0 and cell.y == self.m-1:
            if self.board.board[cell.x][cell.y-1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y-1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y].state == 1:
                num_of_neighbors += 1

        elif cell.x != 0 and cell.y == 0 and cell.x != self.n-1:
            if self.board.board[cell.x-1][cell.y].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x-1][cell.y+1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x][cell.y+1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y+1].state == 1:
                num_of_neighbors += 1

        elif cell.x != 0 and cell.y == 0 and cell.x == self.n-1:
            if self.board.board[cell.x-1][cell.y].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x-1][cell.y+1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x][cell.y+1].state == 1:
                num_of_neighbors += 1

        elif cell.x != 0 and cell.y != 0 and cell.x != self.n-1 and cell.y != self.m-1:
            if self.board.board[cell.x-1][cell.y-1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x-1][cell.y].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x-1][cell.y+1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x][cell.y-1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x][cell.y+1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y-1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x+1][cell.y+1].state == 1:
                num_of_neighbors += 1

        elif cell.x == self.n-1 and cell.y == self.m-1:
            if self.board.board[cell.x-1][cell.y-1].state == 1:
                num_of_neighbors += 1
            if self.board.board[cell.x-1][cell.y].state == 1:
                num_of_neighbors += 1
            elif self.board.board[cell.x][cell.y-1].state == 1:
                num_of_neighbors += 1
        return num_of_neighbors
                
            
            
                
        
