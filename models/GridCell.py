import pygame


class GridCell:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.candidate = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont(None, 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap
        margin = 15

        if self.candidate != 0 and self.value == 0:
            text = fnt.render(str(self.candidate), 1, (128, 128, 128))
            win.blit(text, (x + 5 + margin, y + 5 + margin))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text,
                     (x + (gap / 2 - text.get_width() / 2) + margin, y + (gap / 2 - text.get_height() / 2) + margin))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x + margin, y + margin, gap, gap), 3)

    def draw_change(self, win, g=True):
        fnt = pygame.font.SysFont(None, 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap
        margin = 15

        pygame.draw.rect(win, (255, 255, 255), (x + margin, y + margin, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2) + margin, y + (gap / 2 - text.get_height() / 2) + margin))
        if g:
            pygame.draw.rect(win, (0, 255, 0), (x + margin, y + margin, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x + margin, y + margin, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_candidate(self, val):
        self.candidate = val
