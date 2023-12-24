import pygame as p
import sys
import numpy as np
from tkinter import *
from tkinter.messagebox import showinfo

p.init()

#display settings
WIDTH = 400
HEIGHT = WIDTH
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4
#Color variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BG_COLOR = (28, 179, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

def draw_lines(screen):
    i = SQUARE_SIZE
    p.draw.line(screen, LINE_COLOR, (0, i), (WIDTH, i), LINE_WIDTH)
    p.draw.line(screen, LINE_COLOR, (0, 2*i), (WIDTH, 2*i), LINE_WIDTH)
    p.draw.line(screen, LINE_COLOR, (i, 0), (i, HEIGHT), LINE_WIDTH)
    p.draw.line(screen, LINE_COLOR, (2*i, 0), (2*i, HEIGHT), LINE_WIDTH)

def draw_figures(screen, board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            i = SQUARE_SIZE
            if board[row][col] == 1:
                p.draw.circle(screen, CIRCLE_COLOR, (int(col * i + i//2), int(row * i + i//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                p.draw.line(screen, CROSS_COLOR, (int(col * i + SPACE), int(row * i + i - SPACE)), (col * i + i - SPACE, row * i + SPACE), CROSS_WIDTH)
                p.draw.line(screen, CROSS_COLOR, (int(col * i + SPACE), int(row * i + SPACE)), (col * i + i - SPACE, row * i + i - SPACE), CROSS_WIDTH)

def mark_square(board, row, col, player):
    board[row][col] = player

def available_square(board, row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(board, player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal_win_line(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal_win_line(player)
        return True

    return False

def draw_vertical_win_line(screen, col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    p.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def draw_horizontal_win_line(screen, row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    p.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal_win_line(screen, player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    p.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_desc_diagonal_win_line(screen, player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    p.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart(screen, board):
    screen.fill(BG_COLOR)
    draw_lines(screen)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

def drawText(screen, text):
    font = p.font.SysFont("Helvitca", 32, True, False)
    textObject = font.render(text, 0, p.Color('Black'))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    screen.blit(textObject, textLocation)



#main loop
def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption('Tic Tac Toe')
    screen.fill(BG_COLOR)
    draw_lines(screen)
    player = 1
    game_over = False
    # board
    board = np.zeros((BOARD_ROWS, BOARD_COLS))

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if available_square(board, clicked_row, clicked_col):
                    mark_square(board, clicked_row, clicked_col, player)
                    if check_win(board, player):
                        game_over = True
                    player = player % 2 + 1

                    draw_figures(screen, board)
                    if player == 1 and game_over == True:
                        drawText(screen, 'Player 2 wins')
                    if player == 2 and game_over == True:
                        drawText(screen, 'Player 1 wins')
            if event.type == p.KEYDOWN:
                if event.key == p.K_r:
                    restart(screen, board)
                    player = 1
                    game_over = False

        p.display.update()

if __name__ == '__main__':
    main()