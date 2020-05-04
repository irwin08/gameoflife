class Cell:
    def __init__(self,i,j):
        self.state = 0 #state is 0 for dead, 1 for alive
        self.x = i
        self.y = j

    def change_state(self, n):
        self.state = n
