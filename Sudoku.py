import sys

import pygame
import time

from models.SudokuGrid import SudokuGrid
from Utils import get_digit, redraw_window


def main():
    pygame.init()
    window = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Sudoku App")
    board = SudokuGrid(9, 9, 540, 540, window)
    key = None
    start = time.time() * 1000
    strikes = 0
    while True:

        time_passed = round(time.time() * 1000 - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    board.solve_gui()

                elif event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cells[i][j].candidate != 0:
                        if board.fill_cell(board.cells[i][j].candidate):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")

                elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    board.clear()
                    key = None

                else:
                    key = get_digit(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)
            key = None

        redraw_window(window, board, time_passed, strikes)
        pygame.display.update()


main()
pygame.quit()
