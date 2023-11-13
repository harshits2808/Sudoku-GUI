import pygame

from models.GridCell import GridCell
from Utils import valid, find_empty


class SudokuGrid:
    grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    solved_grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.cells = [[GridCell(self.grid[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.copy = None
        self.update_copy()
        self.selected = None
        self.win = win
        self.solvable = self.solve()

    def update_copy(self):
        self.copy = [[self.cells[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def fill_cell(self, val):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set(val)
            self.update_copy()

            if self.solved_grid[row][col] == val:
                return True
            else:
                self.cells[row][col].set(0)
                self.cells[row][col].set_candidate(0)
                self.update_copy()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cells[row][col].set_candidate(val)

    def draw(self):
        # Draw Grid Lines
        gap = self.width / 9
        margin = 15
        for i in range(self.rows + 1):
            if i % 3 == 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0, 0, 0), (0 + margin, i * gap + margin), (self.width + margin, i * gap + margin), thick)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap + margin, 0 + margin), (i * gap + margin, self.height + margin), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].selected = False

        self.cells[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cells[row][col].value == 0:
            self.cells[row][col].set_candidate(0)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value == 0:
                    return False
        return True

    def solve(self):
        find = find_empty(self.solved_grid)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.solved_grid, i, (row, col)):
                self.solved_grid[row][col] = i

                if self.solve():
                    return True

                self.solved_grid[row][col] = 0

        return False

    def solve_gui(self):
        self.update_copy()
        find = find_empty(self.copy)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.copy, i, (row, col)):
                self.copy[row][col] = i
                self.cells[row][col].set(i)
                self.cells[row][col].draw_change(self.win, True)
                self.update_copy()
                pygame.display.update()
                pygame.time.delay(100)

                if self.solve_gui():
                    return True

                self.copy[row][col] = 0
                self.cells[row][col].set(0)
                self.update_copy()
                self.cells[row][col].draw_change(self.win, False)
                pygame.display.update()
                pygame.time.delay(100)

        return False

