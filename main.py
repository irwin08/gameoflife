import board
import gameoflife
import cell
import pygame
import sys

def draw_bordered_rect(screen, x, y, w, h, color):
    pygame.draw.rect(screen, BLACK, [x,y,w,h])
    pygame.draw.rect(screen, color, [x+4, y+4, w-8, h-8]) #probably should make this not hardcoded

def main():

    window_width = 400
    window_height = 400

    block_size = 20

    margin = 5
    
    screen = pygame.display.set_mode((window_height, window_width))
    
    board = []

    n = window_height//block_size
    m = window_width//block_size

    for i in range(0,n):
        board.append([])
        for j in  range(0,m):
            board[i].append(cell.Cell(i,j))

    board[5][5].state = 1
    board[5][6].state = 1
    board[5][7].state = 1

    board[6][8].state = 1
    board[6][7].state = 1
    board[6][6].state = 1
            
    my_game = gameoflife.GameOfLife(n,m)
    my_game.set_board(board)
    
    my_game.print_board()

    print()

    clock = pygame.time.Clock()

    start = False
    
    while True:
        
        draw_grid(screen, my_game, block_size, margin, n, m)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[0]//(block_size + margin)
                col = pos[1]//(block_size + margin)
                if my_game.board.board[col][row].state == 0:
                    my_game.board.board[col][row].state = 1
                else:
                    my_game.board.board[col][row].state = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = not start

        pygame.display.update()

        if start:
            pygame.time.wait(1000)
            my_game.advance()

def draw_grid(screen, my_game, block_size, margin, n, m):
    white = (200, 200,200)
    red = (200,0,0)

    for row in range(n):
        for col in range(m):
            color = white
            if my_game.board.board[row][col].state == 1:
                color = red
            pygame.draw.rect(screen, color, [(block_size + margin)*col + margin,
                                             (block_size + margin)*row + margin,
                                             block_size, block_size])
                

if __name__ == "__main__":
    main()
