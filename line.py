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
    x_start, y_start = start
    x_stop, y_stop = stop
    WHEN_TO_STOP = 500
    counting = 0
    while counting <= WHEN_TO_STOP:
        percentage = counting / WHEN_TO_STOP
        x = x_start + (x_stop - x_start) * percentage
        y = y_start + (y_stop - y_start) * percentage
        draw_pixel(screen, x, y, BLACK)
        counting += 1


screen = pygame.display.set_mode((SIZE, SIZE))
screen.fill(WHITE)

line((300, 300), (600, 600))

pygame.display.flip()

input()
