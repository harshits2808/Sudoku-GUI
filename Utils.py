import pygame


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j

    return None


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def redraw_window(win, board, time_passed, strikes):
    win.fill((255, 255, 255))
    # Draw time
    fnt = pygame.font.SysFont(None, 40)
    text = fnt.render("Time: " + format_time(time_passed), 1, (0, 0, 0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw()


def format_time(time_passed):
    ms = time_passed % 1000
    sec = (time_passed // 1000) % 60
    minute = (time_passed // 1000) // 60
    hour = minute // 60

    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(sec).zfill(2) + "." + str(ms).zfill(3)


def get_digit(event):
    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
        return 1
    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
        return 2
    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
        return 3
    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
        return 4
    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
        return 5
    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
        return 6
    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
        return 7
    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
        return 8
    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
        return 9
    else:
        return None
