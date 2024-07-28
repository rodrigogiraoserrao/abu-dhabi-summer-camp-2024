import pygame


SIZE = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_pixel(screen, x, y, colour):
    x, y = int(x), int(y)
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            screen.set_at((x + dx, y + dy), colour)


def line(start, stop):
    STEPS = 1000
    x_start, y_start = start
    x_stop, y_stop = stop
    step = 0
    while step <= STEPS:
        percentage = step / STEPS
        x = x_start + (x_stop - x_start) * percentage
        y = y_start + (y_stop - y_start) * percentage
        draw_pixel(screen, x, y, BLACK)
        step += 1


screen = pygame.display.set_mode((SIZE, SIZE))
screen.fill(WHITE)

line((0, 0), (SIZE, SIZE))
line((0, 20), (SIZE, SIZE))
line((0, 40), (SIZE, SIZE))
pygame.display.flip()

input()
